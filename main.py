import tkinter


BLACK = "#000000"
GREY = "#CCCCCC"
WHITE = "#EDEDED"

all_pitches = ["C", "C#/D♭", "D", "D#/E♭", "E", "F", "F#/G♭", "G", "G#/A♭", "A", "A#/B♭", "B"]

pitches = all_pitches

actual_scale = "Major"

all_scales = ["Major", "Minor"]

def get_chords_scales():
    """Return chords and scales to selected tonation"""

    global pitches
    first = root_note.get()
    lst = all_pitches
    pos = lst.index(first)
    pitches = lst[pos:] + lst[:pos]

    # Key
    major_key = [
        pitches[0], pitches[2], pitches[4], pitches[5], pitches[7], pitches[9], pitches[11]
    ]

    minor_key = [
        pitches[0], pitches[2], pitches[3], pitches[5], pitches[7], pitches[8], pitches[10]
    ]

    global actual_scale
    actual_scale = scale.get()

    if actual_scale == "Major":
        scale_degrees_numbers_label.config(text="NUM\n\n"
                                                "I. \n"
                                                "ii. \n"
                                                "iii. \n"
                                                "IV. \n"
                                                "V. \n"
                                                "vi.\n"
                                                "viio. ")
        chords_label.config(text="CHORDS\n\n"
                                f"{major_key[0]} Maj\n"
                                f"{major_key[1]} min\n"
                                f"{major_key[2]} min\n"
                                f"{major_key[3]} Maj\n"
                                f"{major_key[4]} Maj\n"
                                f"{major_key[5]} min\n"
                                f"{major_key[6]} dim")
        scale_degrees_names_label.config(text="DEGREE NAME\n\n"
                                              "Tonic \n"
                                              "Supertonic \n"
                                              "Mediant \n"
                                              "Subdominant \n"
                                              "Dominant \n"
                                              "Submediant \n"
                                              "Leading tone ")
        chord_pitches_label.config(text="CHORD PITCHES\n\n"
                            f"{major_key[0]}   |   {major_key[2]}   |   {major_key[4]}\n"
                            f"{major_key[1]}   |   {major_key[3]}   |   {major_key[5]}\n"
                            f"{major_key[2]}   |   {major_key[4]}   |   {major_key[6]}\n"
                            f"{major_key[3]}   |   {major_key[5]}   |   {major_key[0]}\n"
                            f"{major_key[4]}   |   {major_key[6]}   |   {major_key[1]}\n"
                            f"{major_key[5]}   |   {major_key[0]}   |   {major_key[2]}\n"
                            f"{major_key[6]}   |   {major_key[1]}   |   {major_key[3]}")
        scale_pitches_label.config(text=f"Scale pitches:     {major_key[0]}     {major_key[1]}     {major_key[2]}     "
                                        f"{major_key[3]}     {major_key[4]}     {major_key[5]}     {major_key[6]}")

    elif actual_scale == "Minor":
        scale_degrees_numbers_label.config(text="NUM\n\n"
                                                "i.\n"
                                                "iio. \n"
                                                "III. \n"
                                                "iv. \n"
                                                "v. \n"
                                                "♭VI. \n"
                                                "♭VII. ")
        chords_label.config(text="CHORDS\n\n"
                                f"{minor_key[0]} min\n"
                                f"{minor_key[1]} dim\n"
                                f"{minor_key[2]} Maj\n"
                                f"{minor_key[3]} min\n"
                                f"{minor_key[4]} min\n"
                                f"{minor_key[5]} Maj\n"
                                f"{minor_key[6]} Maj")
        scale_degrees_names_label.config(text="DEGREE NAME\n\n"
                                              "Tonic \n"
                                              "Supertonic \n"
                                              "Mediant \n"
                                              "Subdominant \n"
                                              "Dominant \n"
                                              "Submediant \n"
                                              "Subtonic ")
        chord_pitches_label.config(text="CHORD PITCHES\n\n"
                            f"{minor_key[0]}   |   {minor_key[2]}   |   {minor_key[4]}\n"
                            f"{minor_key[1]}   |   {minor_key[3]}   |   {minor_key[5]}\n"
                            f"{minor_key[2]}   |   {minor_key[4]}   |   {minor_key[6]}\n"
                            f"{minor_key[3]}   |   {minor_key[5]}   |   {minor_key[0]}\n"
                            f"{minor_key[4]}   |   {minor_key[6]}   |   {minor_key[1]}\n"
                            f"{minor_key[5]}   |   {minor_key[0]}   |   {minor_key[2]}\n"
                            f"{minor_key[6]}   |   {minor_key[1]}   |   {minor_key[3]}")

        scale_pitches_label.config(text=f"Scale pitches:     {minor_key[0]}     {minor_key[1]}     {minor_key[2]}     "
                                        f"{minor_key[3]}     {minor_key[4]}     {minor_key[5]}     {minor_key[6]}")

    functional_chord_quality_label.config(text="FUNCTIONAL CHORD\n\n"
                                               "Tonic\n"
                                               "Sub-Dominant\n"
                                               "Tonic / Dominant\n"
                                               "Sub-Dominant\n"
                                               "Dominant\n"
                                               "Tonic / Sub-Dominant\n"
                                               "Dominant")


# Window config
window = tkinter.Tk()
window.resizable(False, False)
window.title("Chords / scales APP")
window.config(padx=30, pady=30, bg=BLACK)

# Frames
options_frame = tkinter.Frame(window, bg=BLACK)
options_frame.pack()
result_frame = tkinter.Frame(window, bg=BLACK)
result_frame.pack()

# Title label
title_label = tkinter.Label(options_frame, text="CHORDS / SCALES APP", font=("Arial", 15, 'bold'),
                            bg=BLACK, fg=WHITE)
title_label.grid(column=0, row=0, columnspan=2, pady=(0, 20))

# Chose root note
root_note_label = tkinter.Label(options_frame, text="Choose root note: ", font=("Arial", 12, 'bold'),
                                bg=BLACK, fg=WHITE)
root_note_label.grid(column=0, row=1)

root_note = tkinter.StringVar()
root_note.set(all_pitches[0])

chosen_root_note = tkinter.OptionMenu(options_frame, root_note, *all_pitches)
chosen_root_note.config(font=("Arial", 12, 'bold'), bg=GREY, activebackground=WHITE, width=8,
                        highlightbackground=BLACK, indicatoron=False)
chosen_root_note["menu"].config(bg=WHITE, fg=BLACK, font=("Arial", 12, 'bold'))
chosen_root_note.grid(column=1, row=1)

# Chose scale
scale_label = tkinter.Label(options_frame, text="Choose scale: ", font=("Arial", 12, 'bold'), bg=BLACK, fg=WHITE)
scale_label.grid(column=0, row=2)

scale = tkinter.StringVar()
scale.set(all_scales[0])

chosen_scale = tkinter.OptionMenu(options_frame, scale, *all_scales)
chosen_scale.config(font=("Arial", 12, 'bold'), bg=GREY, activebackground=WHITE, width=8,
                    highlightbackground=BLACK, indicatoron=False)
chosen_scale["menu"].config(bg=WHITE, fg=BLACK, font=("Arial", 12, 'bold'))
chosen_scale.grid(column=1, row=2)

# Button GET CHORDS
button = tkinter.Button(options_frame, text="🤘🤘🤘 GET CHORDS 🤘🤘🤘",font=("Arial", 15), bg=GREY, activebackground=WHITE,
                        command=get_chords_scales, padx=50)
button.grid(column=0, row=3, columnspan=2, pady=(20, 40))

# Result
scale_degrees_numbers_label = tkinter.Label(result_frame, text="NUM\n\n\n\n\n\n\n\n"
                                            , justify="left", width=5, font=("Arial", 12, 'bold'), bg=BLACK, fg=WHITE)
scale_degrees_numbers_label.grid(column=0, row=0)

chords_label = tkinter.Label(result_frame, text="CHORDS\n\n\n\n\n\n\n\n",
                             justify="left", width=15, font=("Arial", 12, 'bold'), bg=BLACK, fg=WHITE)
chords_label.grid(column=1, row=0)

scale_degrees_names_label = tkinter.Label(result_frame, text="DEGREE NAME\n\n\n\n\n\n\n\n",
                                          justify="left", width=15, font=("Arial", 12, 'bold'), bg=BLACK, fg=WHITE)
scale_degrees_names_label.grid(column=2, row=0)

chord_pitches_label = tkinter.Label(result_frame, text="CHORD PITCHES\n\n\n\n\n\n\n\n",
                                    justify="left", width=25, font=("Arial", 12, 'bold'), bg=BLACK, fg=WHITE)
chord_pitches_label.grid(column=3, row=0)

functional_chord_quality_label = tkinter.Label(result_frame, text="FUNCTIONAL CHORD\n\n\n\n\n\n\n\n",
                                               justify="left", width=20, font=("Arial", 12, 'bold'), bg=BLACK, fg=WHITE)
functional_chord_quality_label.grid(column=4, row=0)

scale_pitches_label = tkinter.Label(result_frame, text="", font=("Arial", 12, 'bold'), bg=BLACK, fg=WHITE)
scale_pitches_label.grid(column=0, row=1, columnspan=5, pady=(40, 0))


window.mainloop()
