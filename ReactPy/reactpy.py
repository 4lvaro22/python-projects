from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

# Componente 
@component
def Item(text, initial_done=False):
    done, set_done = hooks.use_state(initial_done)

    def handle_click(event):
        set_done(not done)

    attrs = { "className": "item", "style": { "color": "green" } } if done else {}
   
    if done:
        return html.li(attrs, text)
    else:
        return html.li(
            html.span(attrs, text),
            html.button({ "on_click": handle_click }, "Done!!")
        )
            

@component
def HelloWorld():
    return html._(
        html.p("My first ReactPy component"),
        html.h1("Hello World"),
        html.ul(
            html.li("This is a test"),
            html.li("or a list"),
            Item("Item 1 this is another component"),
            Item("Learn ReactPy", initial_done=True),
        )
    )

# Crear la aplicacion FastAPI
app = FastAPI()
# configurar la aplicacion 
configure(app, HelloWorld)