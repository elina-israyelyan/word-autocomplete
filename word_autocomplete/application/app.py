import dash
import dash_bootstrap_components as dbc
import decouple
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from dash_extensions import Keyboard

from tree.trie_tree import Trie

tree = Trie()
tree.load_tree(decouple.config("TREE_PATH"))
external_stylesheets = [dbc.themes.CYBORG]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([html.H1(children="Word Autocomplete",
                               id="Title",
                               style={'vertical-align': 'middle', 'width': '49%', 'display': 'inline-block'}),
                       dcc.Input(
                           id="input",
                           type="text",
                           placeholder="Type something...",
                           value=""
                       ),
                       Keyboard(id="keyboard")
                       ])


@app.callback(Output('input', 'value'),
              [Input("keyboard", "n_keydowns"), Input('input', 'value')],
              [State("keyboard", "keydown")],
              )
def change_suggestion(n_keydowns, input_value, event):
    if event['key'] == 'ArrowRight':
        res = tree.autocomplete(input_value)
        return res
    else:
        return input_value


if __name__ == '__main__':
    app.run_server(debug=False)
