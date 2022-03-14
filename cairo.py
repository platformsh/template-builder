# import svg
# canvas = svg.SVG(
#     width=1081,
#     height=259,
#     xmlns="http://www.w3.org/2000/svg",
#     elements=[
#         svg.Circle(
#             cx=30, cy=30, r=20,
#             stroke="red",
#             fill="white",
#             stroke_width=5,
#         ),
#     ],
# )
# print(canvas)

import svg
canvas = svg.SVG(
    width=1081,
    height=259,
    xmlns="http://www.w3.org/2000/svg",
    elements=[
        svg.Rect(
            x=0, y=0, width=1081, height=259, fill='#ffbdbb'
        ),
        svg.Image(
            x=0, y=0, width=500, href='https://s.w.org/style/images/about/WordPress-logotype-standard.png'
        ),
        svg.Image(
            x=0, y=0, width=500, href='https://platform.sh/logos/redesign/Platformsh_logo_black.svg'
        )
    ],
)
print(canvas)