from pyecharts import options as opts
from pyecharts.charts import Pie, Bar,Page
import pandas as pd

data = pd.read_excel('data.xlsx')

YEARS = ['Year:2015', 'Year:2016', 'Year:2017', 'Year:2018','Year:2019','Year:2020','Year:2021']
date = ['Jan 2015', 'Feb 2015','Mar 2015','Apr 2015','May 2015','Jun 2015','Jul 2015','Aug 2015','Sep 2015','Oct 2015','Nov 2015','Dec 2015',
        'Jan 2016', 'Feb 2016','Mar 2016','Apr 2016','May 2016','Jun 2016','Jul 2016','Aug 2016','Sep 2016','Oct 2016','Nov 2016','Dec 2016',
        'Jan 2017', 'Feb 2017','Mar 2017','Apr 2017','May 2017','Jun 2017','Jul 2017','Aug 2017','Sep 2017','Oct 2017','Nov 2017','Dec 2017',
        'Jan 2018', 'Feb 2018','Mar 2018','Apr 2018','May 2018','Jun 2018','Jul 2018','Aug 2018','Sep 2018','Oct 2018','Nov 2018','Dec 2018',
        'Jan 2019', 'Feb 2019','Mar 2019','Apr 2019','May 2019','Jun 2019','Jul 2019','Aug 2019','Sep 2019','Oct 2019','Nov 2019','Dec 2019',
        'Jan 2020', 'Feb 2020','Mar 2020','Apr 2020','May 2020','Jun 2020','Jul 2020','Aug 2020','Sep 2020','Oct 2020','Nov 2020','Dec 2020',
        'Jan 2021', 'Feb 2021','Mar 2021','Apr 2021','May 2021','Jun 2021','Jul 2021','Aug 2021','Sep 2021','Oct 2021','Nov 2021','Dec 2021']

model_3_data = []
for year in YEARS:
    for month in range(12):
        model_3_data.append(data[year][month])

model_S_data = []
for year in YEARS:
    for month in range(12):
        model_S_data.append(data[year][month + 13])

model_X_data = []
for year in YEARS:
    for month in range(12):
        model_X_data.append(data[year][month + 26])

total_3 = sum(model_3_data)
total_s = sum(model_S_data)
total_x = sum(model_X_data)

total = total_3 + total_s + total_x



bar = (
    Bar()
    .add_xaxis(date)
    .add_yaxis("Model S", model_S_data, stack = 'stack1', category_gap="50%")
    .add_yaxis("Model X", model_X_data, stack = 'stack1', category_gap="50%")
    .add_yaxis("Model 3", model_3_data, stack = 'stack1', category_gap="50%")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Number of Sales per Month"),
        datazoom_opts=[opts.DataZoomOpts()]
    )
#     .render("bar_datazoom_both.html")
)

bar.render_notebook()



x_label = ['Model S', 'Model X', 'Model 3']
y_data = [total_s, total_x, total_3]
pie = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(x_label, y_data)],
        radius=["30%", "75%"],
        rosetype="area",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Number of Sales"))
)


pie.render_notebook()
page = Page(layout=Page.DraggablePageLayout)

page.add(
bar,
pie
)

page.render()
