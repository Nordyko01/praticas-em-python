import plotly.express as px

fig = px.bar(x=["A", "B", "C"], y=[20, 30, 45])
fig.write_html("bar_chart.html")
fig.show()