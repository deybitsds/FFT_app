def gui_program():
    pol_1 = program.input_pol_1.text()
    pol_2 = program.input_pol_2.text()
    if pol_1 == "no sé":
        program.msj_error.setText("Guasa")
    elif pol_1 == "si sé":
        gui_resultado()
    else:
        program.msj_error.hide()

