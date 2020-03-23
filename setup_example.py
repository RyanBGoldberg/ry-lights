from ActionBuilder import ActionBuilder

from actions.ActionColor import ActionColor
from actions.ActionStrobe import ActionStrobe
from actions.ActionStrobeMute import ActionStrobeMute
from actions.ActionColorTrigger import ActionColorTrigger
from actions.ActionMute import ActionMute
from actions.ActionChaos import ActionChaos

from Color import Color

def initialize(app, params):
    # Set GPIO pins for R, G, B wires
    params["PIN_R"] = 17
    params["PIN_G"] = 22
    params["PIN_B"] = 24

    # Create Actions
    # Basic Colors
    actionWhite = app.addAction(ActionColor(params))
    actionBlue = app.addAction(ActionColor(params, Color(0, 0, 255)))
    actionGreen = app.addAction(ActionColor(params, Color(0, 255, 0)))
    actionRed = app.addAction(ActionColor(params, Color(255, 0, 0)))

    actionColorTrigger = app.addAction(ActionColorTrigger(params))

    actionStrobe = app.addAction(ActionStrobe(params))
    actionStrobeMute = app.addAction(ActionStrobeMute(params))
    actionMute = app.addAction(ActionMute(params))
    actionChaos = app.addAction(ActionChaos(params))


    # Bind Inputs to Actions
    app.addInput(actionBlue, "knob", 5, "Intensity")
    app.addInput(actionGreen, "knob", 6, "Intensity")
    app.addInput(actionRed, "knob", 7, "Intensity")
    app.addInput(actionWhite, "knob", 8, "Intensity")

    app.addInput(actionStrobe, "knob", 1, "Speed")
    app.addInput(actionStrobe, "knob", 2, "Intensity")
    app.addInput(actionChaos, "knob", 3, "Intensity")


    app.addInput(actionColorTrigger, "trigger_hold", 38, "Sustain")


    # COMMENT 2
    # app.addInput(actionMute, "hold", 45, "On")
    # app.addInput(actionChaos, "hold", 44, "Intensity")
    # app.addInput(actionWhite, "hold", 46, "Intensity")
    # app.addInput(actionStrobeMute, "hold", 47, "On")


    # app.addInput(actionStrobeMute, "knob", 10, "Speed")


    # Use ActionBuilder (optional)
    ActionBuilder.buildKeys(app, 48, 72, Color.red(), Color.blue())
