from typing import Any
from line_plan_visualization.train_lines import Lines
from line_plan_visualization.pyhsical_railway import PhysicalRailWay
from line_plan_visualization.default_appearance import default_appearance
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

class LinePlan(object):
    """
    Parameters:
       physical_railway: A instance of  PhysicalRailWay
       lines: A instance of Lines
    """

    __slots__ = ("__physical_railway", "__lines")

    def __init__(self, physical_railway: PhysicalRailWay, lines: Lines) -> None:
        self.__physical_railway: PhysicalRailWay = self.__check_physical_railway(physical_railway)
        self.__lines: Lines = self.__check_lines(lines)
    
    @property
    def physical_railway(self) -> PhysicalRailWay:
        return self.__physical_railway

    @property
    def lines(self) -> Lines:
        return self.__lines
    
    @staticmethod
    def __check_physical_railway(physical_railway: PhysicalRailWay) -> PhysicalRailWay:
        if not isinstance(physical_railway, PhysicalRailWay):
            raise Exception(f"unexpected {type(physical_railway)} type of {physical_railway}, only 'PhysicalRailWay' type")

        return physical_railway
    
    def __check_lines(self, lines) -> dict[int, list[int]]:
        if not isinstance(lines, Lines):
            raise Exception(f"PhysicalRailWay {type(lines)} of {lines}, only 'Lines' type")

        if len(self.__physical_railway) != len(lines):
            raise Exception("different length of PhysicalRailWay and Lines")
             
        return lines
        
    def draw(self, **kwargs: dict[str, Any]) -> None:
        """
        Parameters:
            figsize: https://matplotlib.org/stable/api/figure_api.html
            dpi: https://matplotlib.org/stable/api/figure_api.html
            pr_marker: stations symbols on the PhysicalRailway
                       'dict' type with Key: "high", "medium" and "low" and Value: marker
                       e.g. pr_marker={"high": 's', "medium": 'o', "low": '.'}
                       https://matplotlib.org/stable/api/markers_api.html
            pr_markercolor: stations symbols colors on the PhysicalRailway
                            'dict' type with Key: "high", "medium" and "low" and Value: color
                            e.g. pr_markercolor={"high": "red", "medium": "purple", "low": "black"}
                            https://matplotlib.org/stable/tutorials/colors/index.html
            pr_markersize: stations symbols size on the PhysicalRailway
                           https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
            pr_linecolor: PhysicalRailway color
                          https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color
            pr_linestyle: PhysicalRailway linestyle
                          https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle
            pr_linewidth: PhysicalRailway linewidth
                          https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth
            pr_position: PhysicalRailway position in the figure
                         https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html
            title_fontsize: PhysicalRailway title font size
                            https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize
            title_fontweight: PhysicalRailway title font weight
                              https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight
            title_fontcolor: PhysicalRailway title font color
                             https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color
            title_fontfamily: PhysicalRailway title font family
                              https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily
            title_va: vertical alignment for PhysicalRailway title
                      https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment
            title_ha: horizontal alignment for PhysicalRailway title
                      https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment
            stations_fontsize: stations names font size
                               https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize
            stations_fontweight: stations names font weight
                                 https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight
            stations_fontcolor: stations names font color               
                                https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color
            stations_fontstyle: stations names font style
                                https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle
            stations_fontfamily: stations names font family
                                 https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily
            stations_ha: horizontal alignment for stations names
                         https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment
            stations_va: vertical alignment for stations names
                         https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment
            lines_marker: stations symbol on the Lines
                          https://matplotlib.org/stable/api/markers_api.html
            lines_markersize: stations symbol size on the Lines
                              https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize
            lines_color: Lines and markers color
                         https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color
            lines_linestyle: Lines linestyle
                             https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle
            lines_linewidth: Lines linewidth
                             https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth
            lines_position: Lines position
                            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position
            arrow_length: Lines arrow length
                          'float' type
                          e.g. arrow_length=0.3
            arrow_width: total width of the full arrow head
                         'float' type
                         e.g. arrow_width=0.2
            ticks_fontsize: Lines ID font size
                            https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize
            ticks_fontcolor: Lines ID font color
                             https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color
            ticks_fontfamily: Lines ID font family
                              https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily
            sta_pr_spacing: spacing between station name and PhysicalRaiway
                            'float' type
                            e.g. sta_pr_spacing=0.005
            title_pr_spacing: spacing between title and PhysicalRaiway
                              'float' type
                              e.g. title_pr_spacing=0.02
        """
        # Only keys in the default_appearance can be passed in as keyword arguments
        self.__check_kwargs(kwargs)
        # Key-value pairs for missing parameters are replaced with key-value pairs for default parameters
        self.__complete_kwargs(kwargs)

        fig: Figure = plt.figure(figsize=kwargs["figsize"], dpi=kwargs["dpi"])
        ax_pr: Axes = fig.add_subplot(2, 1, 1, position=kwargs["pr_position"])
        ax_lines: Axes = fig.add_subplot(2, 1, 2, position=kwargs["lines_position"])

        self.__draw_pr(ax_pr, kwargs)
        self.__draw_lines(ax_lines, kwargs)
 
    def __draw_pr(self, ax_pr: Axes, kwargs: dict[str, Any]) -> None:
        # coor
        x_pr: list[int] = [_ for _ in range(0, len(self.__physical_railway))]
        y_pr: list[int] = [0] * len(self.__physical_railway)
        # set axis off
        ax_pr.set_axis_off()
        # set stations names
        self.__set_stations_names(ax_pr, kwargs, x_pr, y_pr)
        # set title
        self.__set_title(ax_pr, kwargs)
        # scatter stations markers
        self.__scatter_stations_markers(ax_pr, kwargs, x_pr, y_pr)
        # plot pr
        self.__plot_pr(ax_pr, kwargs, x_pr, y_pr)
     
    def __draw_lines(self, ax_lines: Axes, kwargs: dict[str, Any]) -> None:
        # set facecolor
        ax_lines.set_facecolor("none")
        # set ticks
        self.__set_ticks(ax_lines, kwargs)
        # arrows
        self.__set_arrows(ax_lines, kwargs)
        # plot
        self.__plot_lines(ax_lines, kwargs)

    def __complete_kwargs(self, kwargs: dict[str, Any]) -> None:
        have_figsize: int = 0
        if "figsize"in kwargs.keys():
            have_figsize = 1

        addition_kwargs: dict[str, Any] = { para: value for para, value in default_appearance.items() if para not in kwargs.keys()}
        kwargs.update(addition_kwargs)
        if have_figsize == 0:
            kwargs["figsize"] = (len(self.__physical_railway), self.__lines.linesnum)
    
    def __check_kwargs(self, kwargs: dict[str, Any]) -> None:
        for para in kwargs.keys():
            if para not in default_appearance.keys():
                raise Exception(f"unexpected keyword argument \"{para}\"")

    def __set_stations_names(self, ax_pr: Axes, kwargs: dict[str, Any], x_pr: list[int], y_pr: list[int]) -> None:
        for idx, (x, y) in enumerate(zip(x_pr, y_pr)):
            ax_pr.text(x, y + kwargs["sta_pr_spacing"], f"{list(self.__physical_railway.stations.keys())[idx]}",
                       fontsize=kwargs["stations_fontsize"],
                       color=kwargs["stations_fontcolor"],
                       fontstyle=kwargs["stations_fontstyle"],
                       family=kwargs["stations_fontfamily"],
                       ha=kwargs["stations_ha"],
                       va=kwargs["stations_va"])

    def __set_title(self, ax_pr: Axes, kwargs: dict[str, Any]) -> None:
        ax_pr.text(len(self.__physical_railway) / 2, kwargs["title_pr_spacing"], f"{self.__physical_railway.name}",
                   color=kwargs["title_fontcolor"],
                   fontsize=kwargs["title_fontsize"],
                   fontweight=kwargs["title_fontweight"],
                   fontfamily=kwargs["title_fontfamily"],
                   va=kwargs["title_va"],
                   ha=kwargs["title_ha"])

    def __scatter_stations_markers(self, ax_pr: Axes, kwargs: dict[str, Any], x_pr: list[int], y_pr: list[int]) -> None:
        for idx, (_, level) in enumerate(self.__physical_railway):
            ax_pr.scatter(x_pr[idx], y_pr[idx],
                          zorder=1,
                          s=kwargs["pr_markersize"],
                          marker=kwargs["pr_marker"][level],
                          color=kwargs["pr_markercolor"][level])
    
    def __plot_pr(self, ax_pr: Axes, kwargs: dict[str, Any], x_pr: list[int], y_pr: list[int]) -> None:
        ax_pr.plot(x_pr, y_pr, zorder=0,
                   color=kwargs["pr_linecolor"],
                   linestyle=kwargs["pr_linestyle"],
                   linewidth=kwargs["pr_linewidth"])

    def __set_ticks(self, ax_lines: Axes, kwargs: dict[str, Any]) -> None:
        ax_lines.tick_params(direction="in")
        # set xticks
        ax_lines.set_xticks([])
        # set yticks
        ax_lines.set_yticks(ticks=[_ for _ in range(-self.__lines.linesnum + 1, 1)],
                            labels=reversed([line_ID for line_ID, _ in self.__lines]),
                            color=kwargs["ticks_fontcolor"],
                            family=kwargs["ticks_fontfamily"],
                            fontsize=kwargs["ticks_fontsize"])

    def __set_arrows(self, ax_lines: Axes, kwargs: dict[str, Any]) -> None:
         for idx, (_, line) in enumerate(self.__lines):
            dx: float = kwargs["arrow_length"]
            dy: float = 0
            x: float = self.__get_coor_of_line(idx, line)['x'][-1] - dx
            y: float = self.__get_coor_of_line(idx, line)['y'][-1] - dy
            
            ax_lines.arrow(x, y, dx, dy,
                           length_includes_head=True,
                           width=0,
                           head_length=dx,
                           color=kwargs["lines_color"],
                           head_width=kwargs["arrow_width"])
            
    def __plot_lines(self, ax_lines: Axes, kwargs: dict[str, Any]) -> None:
        for idx, (_, line) in enumerate(self.__lines):
            x_line: list[int] = self.__get_coor_of_line(idx, line)['x']
            y_line: list[int] = self.__get_coor_of_line(idx, line)['y']
            ax_lines.plot(x_line, y_line,
                          marker=kwargs["lines_marker"],
                          markersize=kwargs["lines_markersize"],
                          color=kwargs["lines_color"],
                          linestyle=kwargs["lines_linestyle"],
                          linewidth=kwargs["lines_linewidth"])

    @staticmethod
    def __get_coor_of_line(idx: int, line: list[int]) -> dict[str, list[int]]:
        return {'x': [x for x, is_stop in enumerate(line) if is_stop],
                'y': [-idx] * line.count(1)}

    @staticmethod
    def show(*, block: bool=None) -> None:
        """
        Parameters:
            https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
        """
        plt.show(block=block)

    @staticmethod
    def save(*args, **kwargs) -> None:
        """
        Parameters:
            https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html 
        """
        plt.savefig(*args, **kwargs)
