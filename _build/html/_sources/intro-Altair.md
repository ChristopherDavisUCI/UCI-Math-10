# Altair

**Samples**

Here are some examples of the types of charts that can be produced using Altair.  You can see the source code for these in the [First two examples notebook](First-two-examples.ipynb).

* [(Source code)](log-curve) Adding a tooltip, so that when the mouse is over a point, more information is displayed:
![tooltip](images/tooltip.png)

* [(Source code)](Spotify-bar) A bar chart, with artist names along the $x$-axis:
![bars](images/bars.png)

* [(Source code)](Spotify-interactive) An interactive chart, where only the points in the selected region have color:
![interactive gif](images/altair.gif)

**Where to read more**

The syntax for Altair can be intimidating the first time you see it (and the fifth time you see it).

```
alt.Chart(spotify_df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = alt.Color('Energy', scale=alt.Scale(scheme='turbo')),
    tooltip = ["Song Name", "Artist"],
)
```

There are endless possibilities for customization.  Here are some places to read about options, but we recommend that you instead begin going through the [First two examples notebook](First-two-examples.ipynb), and return to these links when there is something specific you want to customize.
* Options for what to draw: [Marks](https://altair-viz.github.io/user_guide/marks.html)
* Different "channels", like `color`, `opacity`, and `size`.  You can see a list of channels here: [Documentation](https://altair-viz.github.io/user_guide/encoding.html#encoding-channels).
* Here is a list of color schemes: [Vega color schemes](https://vega.github.io/vega/docs/schemes/) and an [example](https://altair-viz.github.io/user_guide/customization.html#color-schemes) of how to use a color scheme in Altair.
* Sometimes it helps to explicitly tell Altair what type of data it is: [encoding types](https://altair-viz.github.io/user_guide/encoding.html#encoding-data-types)
* I often find browsing examples easier than reading documentation.  If you're the same way, check out the Altair [example gallery](https://altair-viz.github.io/gallery/index.html).