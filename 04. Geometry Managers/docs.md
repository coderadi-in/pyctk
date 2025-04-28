# Geometry Managers

Geometry Managers in Python CTk control how the widgets are positioned and sized within their parent containers. There are three geometry managers offered by CTk.

1. `pack`: Organizes widgets in vertical/horizontal blocks. Best for simple stacked layouts.
2. `grid`: Arranges widgets in rows and columns. Ideal for structured table-like designs.
3. `place`: Places widgets at exact coordinates. Ideal for pixel-perfect positioning or overlays.

## Key Rules

- Never mix managers in the same parent container.
- Use nested frames to combine managers for complex UIs.

## 01. The Pack Manager

Pack is a geometry manager in Python CTk that organizes widgets in blocks (vertically or horizontally) within their parent containers. It's ideal for simple layouts.

### Common Use-Cases

- **Stacked Layouts**:  Vertical/Horizontal Arrangements.
- **Centered Content**: A simple widget centered in a window.
- **Nested Containers**: Combining frames packed in different directions.
- **Dynamic Resizing**: Widgets that expand with the window.

### Arguments

Argument | Description | Values/Examples | Default
-|-|-|-
side | Side of parent where widget is placed. | `"top"`, `"bottom"`, `"left"`, `"right"` | `"top"`
fill | Fill available space along along the axis. | `"none"`, `"x"`, `"y"`, `"both"` | `"none"`
expand | Allow widget to expand into extra space. | `True`, `False` | `False`
anchor | Position widgets within its allocated space. | `"n"`, `"ne"`, `"e"`, `"se"`, `"s"`, `"sw"`, `"w"` , `"nw"`, `"center"` | `"center"`
padx/pady | External padding (space outside widget) | Pixels (e.g, `5`, `10`) | `0`
ipadx/ipady | Internal padding (space inside widget) | Pixels (e.g, `10`, `(5, 10)`) | `0`

## 02. The Grid Manager

Grid geometry manager organizes widgets in a table-like structure of rows and columns. It provides precise control over widgets placement, making it ideal for complex layouts.

### Common Use-Cases

- **Forms**: Align labels and inputs in rows/columns.
- **Dashboard**: Arrange widgets like buttons, charts, or stats in grid.
- **Spreadsheet-like Layouts**: Display data tables or matrices.

## Arguments

Argument | Description | Values/Examples | Default
-|-|-|-
row | Row number where the widget is placed. | Integers (e.g `0`, `1`) | `0`
column | Column number where the widget is placed. | Integers (e.g `0`, `1`) | `0`
rowspan | Number of rows the widget spans vertically. | Integers (e.g `2`) | `1`
columnspan | Number of columns the widget spans horizontally. | Integers (e.g `3`) | `1`
sticky | Stretches widget to fill its cell | Directions (e.g `"n"`, `"sw"`, `"e"`) | `"center"`
padx/pady | External padding (space outside widget) | Pixels (e.g, `5`, `10`) | `0`
ipadx/ipady | Internal padding (space inside widget) | Pixels (e.g, `10`, `(5, 10)`) | `0`