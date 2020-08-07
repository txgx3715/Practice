from pyecharts.charts import Line
from pyecharts import options as opts
x_data = ['美国',
'巴西',
'英国',
'俄罗斯',
'印度',
'西班牙',
'墨西哥',
'智利',
'伊朗',
'意大利'
]
y_data = [820, 932, 901, 934, 1290, 1330, 1320]


(
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="累计确诊",
        stack="总量",
        y_axis=[2678482,
1368195,
311965,
641156,
567536,
296050,
216852,
275999,
225205,
240436
],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="现有确诊",
        stack="总量",
        y_axis=[1445519,
552419,
267023,
228560,
215360,
70746,
63361,
34270,
28355,
16496
],
        label_opts=opts.LabelOpts(is_show=False),
    )

    .set_global_opts(
        title_opts=opts.TitleOpts(title="折线图堆叠"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("pic6.html")
)