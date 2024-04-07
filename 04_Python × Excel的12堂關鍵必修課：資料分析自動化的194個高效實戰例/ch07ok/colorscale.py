from openpyxl import load_workbook
from openpyxl.formatting.rule import ColorScaleRule


wb = load_workbook('score.xlsx')
target=wb.active

color_scale=ColorScaleRule(
    start_type="min", start_color="0000FF",
    end_type="max", end_color="FFFFFF"
)
target.conditional_formatting.add("B2:B8",color_scale)
                
wb.save('score_colorscale.xlsx')
