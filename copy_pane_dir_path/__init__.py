from fman import DirectoryPaneCommand, show_status_message, clipboard
from fman.url import as_human_readable, dirname, splitscheme

class CopyPaneDirPath(DirectoryPaneCommand):
    def __call__(self):
        pane_path = self.pane.get_path()
        clipboard.clear()
        clipboard.set_text(pane_path)
        clipboard.set_text(splitscheme(pane_path)[1])
        show_status_message('Copied ' + splitscheme(pane_path)[1] + ' to the clipboard', timeout_secs=3)