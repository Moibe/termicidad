import gradio as gr
import yearDivision

#Función principal
def greet(name):

    #yearDivision.divideYear()
        
    return "Tervetuloa " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
