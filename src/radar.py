import plotly.graph_objects as go

fig = go.Figure(go.Scatterpolar(
    name = "Case 42",
    r = [36, 18.5, 186],
    theta = ["bill_length", "bill_depth", "flipper_length"], 
    opacity=0.8
    )
)

fig.add_trace(go.Scatterpolar(
      name = "Case 342",
      r = [50.8, 19, 210],
      theta = ["bill_length", "bill_depth", "flipper_length"], 
      opacity = 0.8
      )
)

fig.add_trace(go.Scatterpolar(
      name = "Case 101",
      r = [41, 20, 203],
      theta = ["bill_length", "bill_depth", "flipper_length"], 
      opacity = 0.8
      )
)

fig.update_traces(fill="toself")

fig.show()

fig2 = go.Figure(go.bar())