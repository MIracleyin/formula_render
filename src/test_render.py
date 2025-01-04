from mathpix_formula import FormulaRenderer, RenderOptions
from manim import WHITE, BLACK

# 使用 Manim 渲染
manim_options = RenderOptions(
    engine='manim',
    image_width=1920,
    image_height=1080,
    quality=90,
    format='png',
    background_color=WHITE,
    tex_color=BLACK,
    scale_factor=1.5,
    output_dir='output/images'
)

renderer = FormulaRenderer(manim_options)

# 测试复杂公式
formula = r'\frac{-b \pm \sqrt{b^2-4ac}}{2a}'
if renderer.is_renderable(formula):
    image_path = renderer.render_to_image(formula)
    print(f'Formula rendered to: {image_path}')
else:
    print('Formula cannot be rendered')

# 使用 Mathpix 渲染
mathpix_options = RenderOptions(
    engine='mathpix',
    image_width=800,
    image_height=600,
    quality=90,
    format='svg'
)

renderer = FormulaRenderer(mathpix_options)
image_url = renderer.render_to_image(formula)
print(f'Mathpix rendered URL: {image_url}') 