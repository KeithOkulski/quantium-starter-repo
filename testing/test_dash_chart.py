from dash_chart import app

def test_title(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.wait_for_element("#title")
    radio = dash_duo.wait_for_element("#location")
    graph_title = dash_duo.wait_for_element("#graph-title")
    dash_duo.wait_for_element("#graph")

    dash_duo.wait_for_element(
        "#graph .js-plotly-plot"
    )

    graph = dash_duo.find_element("#graph .js-plotly-plot")

    assert graph.is_displayed()


    assert header is not None
    assert header.is_displayed()


    assert graph_title is not None
    assert graph_title.is_displayed()


    assert radio is not None
    assert radio.is_displayed()
