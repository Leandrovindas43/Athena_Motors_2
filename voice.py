'''
  For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk 
'''
import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.

class class_voice:
        
    def fun_voice(text):   
        speech_config = speechsdk.SpeechConfig(subscription='172b68e4cf6f4c7e9ddab8641d54ce92', region='eastus')
        # Note: the voice setting will not overwrite the voice element in input SSML.
        speech_config.speech_synthesis_voice_name = "es-MX-BeatrizNeural"
        # use the default speaker as audio output.
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        result = speech_synthesizer.speak_text_async(text).get()
        # Check result
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))



