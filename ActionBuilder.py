from actions.ActionColorTrigger import ActionColorTrigger
from Color import Color
from midi_in.InputControl import InputControl

# A factory class for creating actions and inputs
class ActionBuilder():

	###
	# BuildKeys - creates a range of TriggerHoldKeys that spans between 2 colors
	# low - low key value
	# high - high key value
	# col1 - first color
	# col2 - second color
	###
	@staticmethod
	def buildKeys(app, low, high, col1=Color.white(), col2=Color.white(), attack=0, sustain=50, release=0):
                high += 1
		for i in range(low, high):
			color = Color.interpolate(col1, col2, (float(i-low)/(high-low)))
			action = app.addAction(ActionColorTrigger(app.params, color, attack=attack, sustain=sustain, release=release))
			app.addInput(action, "trigger_hold", i, "")
