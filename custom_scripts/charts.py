import matplotlib
# Force matplotlib to not use any Xwindows backend.
# matplotlib.use('Agg')

import logging
import pandas as pd
import os
import six
import matplotlib.pyplot as plt



fm = matplotlib.font_manager
rcParams = matplotlib.rcParams
fpath = os.path.join(os.path.dirname(__file__), '../config/fonts/Akshar Unicode.ttf')
prop = fm.FontProperties(fname=fpath)

# Set Logging Level
logging.getLogger().setLevel(logging.INFO)

class CustomException(Exception):
    pass


def generate_table_subplot(table_data: list, plot_position: dict, title: str, column_name_lines: int, figure):
    table_df = pd.DataFrame(table_data)
    subplot = figure.add_subplot(plot_position['row_number'], plot_position['column_number'], plot_position['chart_number'])
    subplot.set_title(title)
    subplot.axis('off')
    rows = None
    cols = table_df.columns
    table = subplot.table(cellText=table_df.values, colLabels=cols, rowLabels=rows, loc='upper center', cellLoc='center')
    table.auto_set_font_size(False)
    table.scale(1.5, 1.5)
    table.auto_set_column_width(col=list(range(len(table_df.columns))))
    header_color='#000000'
    row_colors=['#f1f1f2', 'w']
    edge_color='w'
    for k, cell in six.iteritems(table._cells):
        cell.set_edgecolor(edge_color)
        cell.set_text_props(fontproperties=prop)
        if k[0] == 0 or k[1] < 0:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
            if column_name_lines > 1:
                cell.set_height((column_name_lines - 1)/10)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return figure
    

def generate_line_chart_subplot(chart_data: dict, plot_position: dict, axis: dict, title: str, x_axis_label_tilt_angle: int, line_point_label: bool, figure):
    subplot = figure.add_subplot(plot_position['row_number'], plot_position['column_number'], plot_position['chart_number'])
    for line_category, line_data in chart_data.items():
        line_df = pd.DataFrame(line_data)    
        subplot.plot(line_df[axis['X']], line_df[axis['Y']], label = line_category, marker='o')
        if line_point_label:
            for x,y in zip(line_df[axis['X']], line_df[axis['Y']]):
                label = "{}".format(y)
                subplot.annotate(label, (x,y), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    subplot.set_xlabel(axis['X'].replace('_', ' '))
    subplot.set_ylabel(axis['Y'].replace('_', ' '))
    subplot.set_xticks(line_df[axis['X']])
    subplot.set_xticklabels(line_df[axis['X']], rotation=x_axis_label_tilt_angle)
    subplot.set_title(title)
    subplot.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    return figure


def generate_plot_image(image_file_path: str, plot_configuration):
    figure= plt.figure()
    for subplot in plot_configuration:
        if subplot.get('type') == 'table':
            figure = generate_table_subplot(subplot.get('plot_data'), subplot.get('plot_position'), subplot.get('title'), subplot.get('column_name_lines'), figure)
        elif subplot.get('type') == 'line_chart':
            figure = generate_line_chart_subplot(subplot.get('plot_data'), subplot.get('plot_position'), subplot.get('axis'), subplot.get('title'), subplot.get('x_axis_label_tilt_angle'), subplot.get('line_point_label'), figure)
        else:
            raise CustomException('Passed type of chart has not been implemented Yet.')
    plt.savefig('{}'.format(image_file_path), format='png',bbox_inches='tight')
    plt.close(figure)
    