"""
Pasapelota — simulación gráfica en Python con tkinter.

Misma lógica del juego de rondas y puntos, ahora con canvas propio
(sin depender del navegador). Los jugadores se dibujan en fila de
pares enfrentados (0 frente a 1, 2 frente a 3, ...) y una pelota
viaja en zigzag entre ellos.
"""

import tkinter as tk

# ---------------------------------------------------------------
# Paleta de colores (los mismos tonos que la versión web, para que
# ambas se vean "de la misma familia")
# ---------------------------------------------------------------
C_PAPER       = "#FBF3E6"
C_INK         = "#2A1B10"
C_WOOD_LIGHT  = "#C88A4C"
C_WOOD_DARK   = "#A66E36"
C_LINE_WHITE  = "#F5EDE0"
C_SCOREBOARD  = "#1B140F"
C_LED_AMBER   = "#FFB13D"
C_LED_DIM     = "#6B4A22"
C_SUMA_GREEN  = "#4F9D69"
C_RESTA_RED   = "#C1443D"
C_BALL        = "#E8592B"
C_BALL_SHADOW = "#A13D1D"

FONT_TITLE  = ("Georgia", 22, "bold")
FONT_SUB    = ("Segoe UI", 9)
FONT_LABEL  = ("Segoe UI", 9, "bold")
FONT_INPUT  = ("Consolas", 12)
FONT_SCORE  = ("Consolas", 22, "bold")
FONT_SCORE_LABEL = ("Consolas", 9)
FONT_PLAYER = ("Segoe UI", 10, "bold")
FONT_DELTA  = ("Consolas", 9, "bold")
FONT_BTN    = ("Segoe UI", 10, "bold")

TICK_MS = 16  # ~60 fps para la animación de la pelota


class Pasapelota(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pasapelota — simulación de rondas y puntos")
        self.configure(bg=C_PAPER)
        self.resizable(False, False)

        # ---- estado del juego (equivalente a tus variables de Python) ----
        self.jugadores = 12
        self.max_puntos = 12
        self.i = 0
        self.puntos = 0
        self.ronda = 1
        self.running = False
        self.finished = False

        # ---- estado de la animación de la pelota ----
        self.positions = []          # (x, y) de cada jugador en el canvas
        self.ball_from = 0
        self.ball_to = 0
        self.ball_t = 1.0            # progreso 0..1 del tramo actual
        self.ball_moving = False
        self.ball_duration_ms = 450
        self.on_arrive = None        # callback cuando la pelota llega
        self.floaters = []           # textos "+2"/"-1" flotando

        self._build_ui()
        self._recompute_layout()
        self._reset_game()
        self._tick()

    # ================================================================
    # Construcción de la interfaz
    # ================================================================
    def _build_ui(self):
        pad = 16

        # --- encabezado ---
        header = tk.Frame(self, bg=C_PAPER)
        header.pack(fill="x", padx=pad, pady=(pad, 6))
        tk.Label(header, text="PASAPELOTA", font=FONT_TITLE,
                 bg=C_PAPER, fg=C_INK).pack(side="left")
        tk.Label(header, text="La pelota recorre a los jugadores en\n"
                               "fila de pares, uno frente al otro.",
                 font=FONT_SUB, bg=C_PAPER, fg="#6b5842",
                 justify="left").pack(side="left", padx=(16, 0))

        # --- configuración (jugadores / máx puntos / leyenda) ---
        config = tk.Frame(self, bg=C_PAPER)
        config.pack(fill="x", padx=pad, pady=(0, 8))

        tk.Label(config, text="Jugadores", font=FONT_LABEL,
                 bg=C_PAPER, fg="#7a6650").grid(row=0, column=0, sticky="w")
        self.var_jugadores = tk.StringVar(value="12")
        tk.Entry(config, textvariable=self.var_jugadores, width=5,
                  font=FONT_INPUT, relief="solid", bd=2
                  ).grid(row=1, column=0, sticky="w", padx=(0, 24))

        tk.Label(config, text="Máx. puntos", font=FONT_LABEL,
                 bg=C_PAPER, fg="#7a6650").grid(row=0, column=1, sticky="w")
        self.var_max = tk.StringVar(value="12")
        tk.Entry(config, textvariable=self.var_max, width=5,
                  font=FONT_INPUT, relief="solid", bd=2
                  ).grid(row=1, column=1, sticky="w", padx=(0, 24))

        legend = tk.Frame(config, bg=C_PAPER)
        legend.grid(row=0, column=2, rowspan=2, sticky="w", padx=(20, 0))
        tk.Label(legend, text="\u25CF par -> +2", font=FONT_SUB,
                 bg=C_PAPER, fg=C_SUMA_GREEN).pack(anchor="w")
        tk.Label(legend, text="\u25CF impar -> -1", font=FONT_SUB,
                 bg=C_PAPER, fg=C_RESTA_RED).pack(anchor="w")

        tk.Button(config, text="Aplicar", font=FONT_BTN,
                  command=self._on_config_change, bg="white", fg=C_INK,
                  relief="solid", bd=2, padx=10
                  ).grid(row=0, column=3, rowspan=2, sticky="e", padx=(30, 0))
        config.grid_columnconfigure(4, weight=1)

        # --- marcador estilo scoreboard ---
        score = tk.Frame(self, bg=C_SCOREBOARD, padx=18, pady=10)
        score.pack(fill="x", padx=pad, pady=(0, 10))

        self.lbl_ronda = self._score_metric(score, "RONDA", "01")
        self.lbl_jugador = self._score_metric(score, "JUGADOR", "00")
        self.lbl_puntos = self._score_metric(score, "PUNTOS", "00")
        self.lbl_delta = self._score_metric(score, "ÚLTIMA JUGADA", "—")
        self.lbl_estado = tk.Label(score, text="LISTO", font=FONT_SCORE_LABEL,
                                    bg="black", fg=C_LED_AMBER, padx=10, pady=4)
        self.lbl_estado.pack(side="right")

        # --- cancha (canvas) ---
        court_frame = tk.Frame(self, bg=C_INK, bd=3)
        court_frame.pack(padx=pad, pady=(0, 10))
        self.canvas = tk.Canvas(court_frame, width=640, height=400,
                                 bg=C_WOOD_LIGHT, highlightthickness=0)
        self.canvas.pack()

        # --- controles ---
        controls = tk.Frame(self, bg=C_PAPER)
        controls.pack(fill="x", padx=pad, pady=(0, 6))

        self.btn_iniciar = tk.Button(controls, text="\u25B6 Iniciar", font=FONT_BTN,
                                      bg=C_BALL, fg="white", relief="solid", bd=2,
                                      padx=12, pady=6, command=self._on_iniciar)
        self.btn_iniciar.pack(side="left", padx=(0, 8))

        self.btn_pausar = tk.Button(controls, text="\u23F8 Pausar", font=FONT_BTN,
                                     bg="white", fg=C_INK, relief="solid", bd=2,
                                     padx=12, pady=6, command=self._on_pausar,
                                     state="disabled")
        self.btn_pausar.pack(side="left", padx=(0, 8))

        self.btn_paso = tk.Button(controls, text="\u23ED Paso a paso", font=FONT_BTN,
                                   bg="white", fg=C_INK, relief="solid", bd=2,
                                   padx=12, pady=6, command=self._on_paso)
        self.btn_paso.pack(side="left", padx=(0, 8))

        self.btn_reiniciar = tk.Button(controls, text="\u21BA Reiniciar", font=FONT_BTN,
                                        bg="white", fg=C_INK, relief="solid", bd=2,
                                        padx=12, pady=6, command=self._reset_game)
        self.btn_reiniciar.pack(side="left", padx=(0, 8))

        tk.Label(controls, text="Velocidad", font=FONT_SUB,
                 bg=C_PAPER, fg="#6b5842").pack(side="left", padx=(24, 4))
        self.var_velocidad = tk.IntVar(value=800)
        tk.Scale(controls, from_=300, to=1800, orient="horizontal",
                 variable=self.var_velocidad, length=140, showvalue=False,
                 bg=C_PAPER, highlightthickness=0).pack(side="left")

        # --- mensaje ---
        self.lbl_msg = tk.Label(self, text="", font=FONT_SUB, bg=C_PAPER,
                                 fg="#6b5842", anchor="w")
        self.lbl_msg.pack(fill="x", padx=pad, pady=(0, pad))

    def _score_metric(self, parent, label, value):
        box = tk.Frame(parent, bg=C_SCOREBOARD)
        box.pack(side="left", padx=(0, 26))
        tk.Label(box, text=label, font=FONT_SCORE_LABEL, bg=C_SCOREBOARD,
                 fg=C_LED_DIM).pack(anchor="w")
        lbl = tk.Label(box, text=value, font=FONT_SCORE, bg=C_SCOREBOARD,
                        fg=C_LED_AMBER)
        lbl.pack(anchor="w")
        return lbl

    # ================================================================
    # Layout de jugadores (misma fórmula que la versión web)
    # ================================================================
    def _recompute_layout(self):
        rows = (self.jugadores - 1) // 2 + 1
        left_x, right_x = 170, 470
        top_pad, row_h = 70, 100
        height = top_pad * 2 + (rows - 1) * row_h
        self.canvas.config(height=height)

        self.positions = []
        for idx in range(self.jugadores):
            row = idx // 2
            col = idx % 2
            x = left_x if col == 0 else right_x
            y = top_pad + row * row_h
            self.positions.append((x, y))

    # ================================================================
    # Estado / reglas del juego (idéntico a tu versión de consola)
    # ================================================================
    @staticmethod
    def _delta_de(indice):
        return -1 if indice % 2 != 0 else 2

    def _leer_config(self):
        def clamp(valor, minimo, maximo, por_defecto):
            try:
                n = int(valor)
            except ValueError:
                return por_defecto
            return max(minimo, min(maximo, n))

        self.jugadores = clamp(self.var_jugadores.get(), 2, 24, 12)
        self.max_puntos = clamp(self.var_max.get(), 1, 999, 12)
        self.var_jugadores.set(str(self.jugadores))
        self.var_max.set(str(self.max_puntos))

    def _on_config_change(self):
        self._reset_game()

    def _reset_game(self):
        self._leer_config()
        self._recompute_layout()

        self.i = 0
        self.puntos = 0
        self.ronda = 1
        self.running = False
        self.finished = False

        self.ball_from = 0
        self.ball_to = 0
        self.ball_t = 1.0
        self.ball_moving = False
        self.on_arrive = None
        self.floaters = []

        self._actualizar_marcador()
        self._actualizar_botones()
        self.lbl_msg.config(text="Listo para empezar. Presioná Iniciar o "
                                  "avanzá Paso a paso.")
        self._draw()

    def _actualizar_marcador(self):
        self.lbl_ronda.config(text=f"{self.ronda:02d}")
        self.lbl_jugador.config(text="—" if self.finished else f"{self.i:02d}")
        self.lbl_puntos.config(text=f"{self.puntos:02d}")
        self.lbl_estado.config(
            text="TERMINADO" if self.finished else ("JUGANDO" if self.running else "PAUSADO")
        )

    def _actualizar_delta(self, delta):
        texto = f"+{delta}" if delta > 0 else str(delta)
        color = C_SUMA_GREEN if delta > 0 else C_RESTA_RED
        self.lbl_delta.config(text=texto, fg=color)

    def _actualizar_botones(self):
        self.btn_iniciar.config(state="disabled" if (self.running or self.finished) else "normal")
        self.btn_pausar.config(state="normal" if self.running else "disabled")
        paso_ok = not (self.running or self.finished or self.ball_moving)
        self.btn_paso.config(state="normal" if paso_ok else "disabled")

    def _agregar_flotante(self, indice, delta):
        x, y = self.positions[indice]
        self.floaters.append({
            "x": x, "y": y - 40,
            "text": f"+{delta}" if delta > 0 else str(delta),
            "color": C_SUMA_GREEN if delta > 0 else C_RESTA_RED,
            "alpha": 1.0,
        })

    def _jugar_turno(self):
        """Equivalente a una vuelta del while True: True original."""
        if self.finished or self.ball_moving:
            return

        indice = self.i
        delta = self._delta_de(indice)
        self.puntos += delta
        self._actualizar_delta(delta)
        self._agregar_flotante(indice, delta)

        siguiente = indice + 1
        va_a_terminar = False

        if siguiente == self.jugadores:
            if self.puntos < self.max_puntos:
                siguiente = 0
                self.ronda += 1
            else:
                va_a_terminar = True

        if va_a_terminar:
            self.finished = True
            self.running = False
            self._actualizar_marcador()
            self._actualizar_botones()
            self.lbl_msg.config(
                text=f"¡Meta alcanzada! Terminó en la ronda {self.ronda}, "
                     f"jugador {indice}, con {self.puntos} puntos."
            )
            return

        self._actualizar_marcador()
        self._actualizar_botones()

        self.ball_from = indice
        self.ball_to = siguiente
        self.ball_t = 0.0
        self.ball_moving = True
        self.ball_duration_ms = self.var_velocidad.get() * 0.55

        def al_llegar():
            self.i = siguiente
            self._actualizar_botones()
            if self.running:
                pausa = max(120, int(self.var_velocidad.get() * 0.35))
                self.after(pausa, self._jugar_turno)

        self.on_arrive = al_llegar

    # ================================================================
    # Botones
    # ================================================================
    def _on_iniciar(self):
        if self.finished:
            return
        self.running = True
        self._actualizar_marcador()
        self._actualizar_botones()
        self.lbl_msg.config(text="Jugando automáticamente…")
        self._jugar_turno()

    def _on_pausar(self):
        self.running = False
        self._actualizar_marcador()
        self._actualizar_botones()
        self.lbl_msg.config(text="En pausa.")

    def _on_paso(self):
        if self.running:
            return
        self.lbl_msg.config(text="Modo paso a paso.")
        self._jugar_turno()

    # ================================================================
    # Bucle de animación (equivalente al requestAnimationFrame de la web)
    # ================================================================
    def _tick(self):
        if self.ball_moving:
            self.ball_t += TICK_MS / self.ball_duration_ms
            if self.ball_t >= 1:
                self.ball_t = 1.0
                self.ball_moving = False

        vivos = []
        for f in self.floaters:
            f["y"] -= 0.028 * TICK_MS
            f["alpha"] -= TICK_MS / 900
            if f["alpha"] > 0:
                vivos.append(f)
        self.floaters = vivos

        self._draw()

        if not self.ball_moving and self.ball_t == 1.0 and self.on_arrive:
            callback = self.on_arrive
            self.on_arrive = None
            callback()

        self.after(TICK_MS, self._tick)

    @staticmethod
    def _ease_in_out(t):
        return 2 * t * t if t < 0.5 else 1 - ((-2 * t + 2) ** 2) / 2

    def _ball_pos(self):
        ax, ay = self.positions[self.ball_from]
        bx, by = self.positions[self.ball_to]
        t = self._ease_in_out(self.ball_t)
        return ax + (bx - ax) * t, ay + (by - ay) * t

    # ================================================================
    # Dibujo
    # ================================================================
    def _draw(self):
        c = self.canvas
        c.delete("all")
        w = int(c["width"])
        h = int(c["height"])

        # piso de madera a rayas
        plank = 22
        y = 0
        franja = 0
        while y < h:
            color = C_WOOD_LIGHT if franja % 2 == 0 else C_WOOD_DARK
            c.create_rectangle(0, y, w, y + plank, fill=color, outline="")
            y += plank
            franja += 1

        # línea divisoria central ("la red")
        c.create_line(w / 2, 20, w / 2, h - 20, fill=C_LINE_WHITE,
                       dash=(2, 8), width=2)

        # camino punteado entre jugadores consecutivos
        for idx in range(len(self.positions) - 1):
            x1, y1 = self.positions[idx]
            x2, y2 = self.positions[idx + 1]
            c.create_line(x1, y1, x2, y2, fill=C_LINE_WHITE, dash=(1, 7), width=2)

        # jugadores
        for idx, (x, y) in enumerate(self.positions):
            es_actual = (not self.finished) and idx == self.i
            ya_jugo = idx < self.i or (self.finished and idx <= self.i)

            if es_actual:
                c.create_oval(x - 32, y - 32, x + 32, y + 32,
                               outline=C_BALL, width=2)

            relleno = "white" if ya_jugo else C_PAPER
            borde = C_BALL if es_actual else C_INK
            grosor = 4 if es_actual else 2
            c.create_oval(x - 26, y - 26, x + 26, y + 26,
                           fill=relleno, outline=borde, width=grosor)
            c.create_text(x, y, text=str(idx), font=FONT_PLAYER, fill=C_INK)

            signo = "+2" if idx % 2 == 0 else "-1"
            color_signo = C_SUMA_GREEN if idx % 2 == 0 else C_RESTA_RED
            c.create_text(x, y + 40, text=signo, font=FONT_DELTA, fill=color_signo)

        # pelota
        bx, by = self._ball_pos()
        c.create_oval(bx - 13, by + 3 - 13, bx + 13, by + 3 + 13,
                       fill="black", outline="", stipple="gray25")
        c.create_oval(bx - 12, by - 12, bx + 12, by + 12,
                       fill=C_BALL, outline=C_BALL_SHADOW, width=2)
        c.create_line(bx - 8, by, bx + 8, by, fill=C_BALL_SHADOW)
        c.create_line(bx, by - 8, bx, by + 8, fill=C_BALL_SHADOW)

        # textos flotantes (+2 / -1 subiendo y desvaneciéndose)
        for f in self.floaters:
            c.create_text(f["x"], f["y"], text=f["text"],
                           font=FONT_DELTA, fill=f["color"])


if __name__ == "__main__":
    app = Pasapelota()
    app.mainloop()
    
        