import wx
from traitsui.wx.text_editor import CustomEditor
from traitsui.editors.text_editor import ToolkitEditorFactory

class _MyTextEditor(CustomEditor):
    def init(self, parent):
        CustomEditor.init(self, parent)
        font = wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.control.SetFont(font)

class MyTextEditor(ToolkitEditorFactory):
    klass = _MyTextEditor
    def _get_custom_editor_class(self):
        return _MyTextEditor
    def _get_simple_editor_class(self):
        return _MyTextEditor

if __name__ == "__main__":
    from traitsui.api import View, Item
    from traits.api import Str, HasTraits

    class MyTestcase(HasTraits):
        a_string = Str()
        traits_view = View(Item('a_string', editor=MyTextEditor()))

    w = MyTestcase()
    w.configure_traits()