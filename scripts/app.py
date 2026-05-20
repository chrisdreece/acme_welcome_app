from pathlib import Path
import sys

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dash import Dash, Input, Output, State, callback_context, dcc, html

from scripts.openai_client import get_assistant_reply


OFFICE_SIZE_OPTIONS = [
    {"id": "office-size-small", "label": "1-19 people"},
    {"id": "office-size-medium", "label": "20-199 people"},
    {"id": "office-size-large", "label": "200+ people"},
]


def initial_messages() -> list[dict]:
    return [
        {
            "role": "assistant",
            "text": "Welcome to Acme Watercoolers! Let's figure out the right hydration setup for your workplace. About how many people use your office?",
        }
    ]


def render_messages(messages: list[dict]):
    return [
        html.Div(
            html.Div(item["text"], className=f"chat-bubble {'assistant' if item['role'] == 'assistant' else 'user'}"),
            className=f"chat-row {'assistant' if item['role'] == 'assistant' else 'user'}",
        )
        for item in messages
    ]


app = Dash(__name__)
app.title = "Acme Watercoolers Welcome App"

app.layout = html.Div(
    [
        dcc.Store(id="chat-messages", data=initial_messages()),
        dcc.Store(id="office-size-selected", data=False),
        html.Div(
            [
                html.P("Acme Watercoolers", className="eyebrow"),
                html.H1("Welcome Agent", className="hero-title"),
                html.P(
                    "Welcome to Acme Watercoolers. Let's find the right office hydration setup for your team.",
                    className="hero-copy",
                ),
            ],
            className="hero-block",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H2("Conversation", className="panel-title"),
                        html.Div(id="chat-transcript", className="chat-transcript", children=render_messages(initial_messages())),
                        html.Div(
                            [
                                html.P("About how many people use your office?", className="selector-label"),
                                html.Div(
                                    [
                                        html.Button(option["label"], id=option["id"], n_clicks=0, className="office-size-button")
                                        for option in OFFICE_SIZE_OPTIONS
                                    ],
                                    className="office-size-button-row",
                                ),
                            ],
                            id="office-size-selector",
                            className="office-size-selector",
                        ),
                        dcc.Textarea(
                            id="user-input",
                            value="",
                            placeholder="Type your question or tell the assistant about your workplace...",
                            className="request-input",
                        ),
                        html.Div(
                            [
                                html.Button("Send", id="send-button", n_clicks=0, className="primary-button"),
                                html.Button("Reset", id="reset-button", n_clicks=0, className="secondary-button"),
                            ],
                            className="button-row",
                        ),
                    ],
                    className="panel chat-panel",
                )
            ],
            className="content-grid",
        ),
    ],
    className="app-shell",
)


@app.callback(
    Output("chat-transcript", "children"),
    Output("chat-messages", "data"),
    Output("user-input", "value"),
    Output("office-size-selected", "data"),
    Input("send-button", "n_clicks"),
    Input("reset-button", "n_clicks"),
    *(Input(option["id"], "n_clicks") for option in OFFICE_SIZE_OPTIONS),
    State("user-input", "value"),
    State("chat-messages", "data"),
    State("office-size-selected", "data"),
    prevent_initial_call=True,
)
def handle_chat(send_clicks, reset_clicks, *args):
    triggered_id = callback_context.triggered[0]["prop_id"].split(".")[0]
    user_input = args[-3]
    chat_messages = list(args[-2] or initial_messages())
    office_size_selected = bool(args[-1])

    if triggered_id == "reset-button":
        messages = initial_messages()
        return render_messages(messages), messages, "", False

    office_size_map = {
        "office-size-small": "About 1 to 19 people use our office.",
        "office-size-medium": "About 20 to 199 people use our office.",
        "office-size-large": "200 or more people use our office.",
    }

    if triggered_id in office_size_map:
        text = office_size_map[triggered_id]
        api_messages = [{"role": item["role"], "content": item["text"]} for item in chat_messages]
        api_messages.append({"role": "user", "content": text})
        reply = get_assistant_reply(api_messages)

        chat_messages.append({"role": "user", "text": text})
        chat_messages.append({"role": "assistant", "text": reply})

        return render_messages(chat_messages), chat_messages, "", True

    text = (user_input or "").strip()
    if not text:
        return render_messages(chat_messages), chat_messages, "", office_size_selected

    api_messages = [{"role": item["role"], "content": item["text"]} for item in chat_messages]
    api_messages.append({"role": "user", "content": text})
    reply = get_assistant_reply(api_messages)

    chat_messages.append({"role": "user", "text": text})
    chat_messages.append({"role": "assistant", "text": reply})

    return render_messages(chat_messages), chat_messages, "", office_size_selected


@app.callback(
    Output("office-size-selector", "style"),
    Input("office-size-selected", "data"),
)
def toggle_office_size_selector(office_size_selected):
    if office_size_selected:
        return {"display": "none"}
    return {"display": "block"}


app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body { margin: 0; font-family: Georgia, "Times New Roman", serif; background: linear-gradient(180deg, #f3efe6 0%, #efe3d1 100%); color: #1f2a33; }
            .app-shell { max-width: 1100px; margin: 0 auto; padding: 28px 24px 40px; }
            .hero-block { background: radial-gradient(circle at top left, #264d73 0%, #18304b 58%, #102132 100%); color: #f9f4eb; border-radius: 28px; padding: 30px 34px; margin-bottom: 22px; box-shadow: 0 18px 50px rgba(16,33,50,0.18); }
            .eyebrow { margin: 0 0 10px; font-size: 13px; letter-spacing: 0.18em; text-transform: uppercase; color: #d4e3f2; }
            .hero-title { margin: 0 0 12px; font-size: 42px; line-height: 1.02; }
            .hero-copy { margin: 0; font-size: 18px; line-height: 1.6; max-width: 60ch; }
            .panel { background: rgba(255,251,245,0.92); border: 1px solid rgba(24,58,90,0.12); border-radius: 24px; box-shadow: 0 16px 40px rgba(77,62,41,0.08); }
            .chat-panel { padding: 24px; }
            .panel-title { margin: 0 0 12px; font-size: 26px; color: #17324d; }
            .content-grid { display: grid; grid-template-columns: 1fr; gap: 22px; }
            .chat-transcript { background: #fffdf8; border: 1px solid rgba(24,58,90,0.1); border-radius: 20px; padding: 16px; min-height: 360px; max-height: 560px; overflow-y: auto; margin-bottom: 14px; }
            .office-size-selector { margin-bottom: 14px; padding: 18px; background: #fff8ef; border: 1px solid rgba(24,58,90,0.1); border-radius: 20px; }
            .selector-label { margin: 0 0 12px; font-size: 15px; color: #17324d; }
            .office-size-button-row { display: flex; gap: 10px; flex-wrap: wrap; }
            .office-size-button { border: 1px solid #17324d; border-radius: 999px; padding: 11px 16px; font-size: 15px; cursor: pointer; background: #f8f5ef; color: #17324d; }
            .chat-row { display: flex; margin-bottom: 10px; }
            .chat-row.assistant { justify-content: flex-start; }
            .chat-row.user { justify-content: flex-end; }
            .chat-bubble { max-width: 85%; border-radius: 18px; padding: 12px 15px; line-height: 1.55; font-size: 15px; white-space: pre-wrap; }
            .chat-bubble.assistant { background: #f0e6d7; color: #2f2417; border-top-left-radius: 6px; }
            .chat-bubble.user { background: #17324d; color: #f8f5ef; border-top-right-radius: 6px; }
            .request-input { width: 100%; min-height: 120px; border-radius: 18px; border: 1px solid #cdbda8; padding: 18px; font-size: 16px; line-height: 1.5; resize: vertical; background: #fffdf8; box-sizing: border-box; }
            .button-row { display: flex; gap: 12px; margin-top: 16px; flex-wrap: wrap; }
            .primary-button, .secondary-button { border: none; border-radius: 999px; padding: 12px 18px; font-size: 15px; cursor: pointer; }
            .primary-button { background: #17324d; color: #f8f5ef; }
            .secondary-button { background: #d9c4a4; color: #3d2c17; }
            @media (max-width: 700px) {
                .hero-title { font-size: 34px; }
                .office-size-button-row { flex-direction: column; }
                .office-size-button { width: 100%; }
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
