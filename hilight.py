import gtk
import gedit

ui_str = """<ui>
	<menubar name="MenuBar">
		<menu name="ToolsMenu" action="Tools">
			<placeholder name="ToolsOps_2">
				<menuitem name="HighlightSelection" action="HighlightSelection"/>
			</placeholder>
		</menu>
	</menubar>
</ui>
"""
	
class HilightPyWindowHelper():
	def __init__(self, plugin, window):
		self._window = window
		self._plugin = plugin
		self._insert_menu()
		self.update_ui()

	def deactivate(self):
		self._remove_menu()
		self._window = None
		self._plugin = None
		self._action_group = None

	def _insert_menu(self):
		manager = self._window.get_ui_manager()
		self._action_group = gtk.ActionGroup("Hilight")
		self._action_group.add_actions([("HighlightSelection", None, _("Highlight Selection"), "<Alt>D", _("Highlight Selection"), lambda a: self.hilight())])
		manager.insert_action_group(self._action_group, -1)
		self._ui_id = manager.add_ui_from_string(ui_str)

	def _remove_menu(self):
		manager = self._window.get_ui_manager()
		manager.remove_ui(self._ui_id)
		manager.remove_action_group(self._action_group)
		manager.ensure_update()

	def update_ui(self):
		print "Update UI"

	def hilight(self,action=None,start=None,end=None):
		print "Hilight selection"


class HilightPyPlugin(gedit.Plugin):
	def __init__(self):
		gedit.Plugin.__init__(self)
		self._instances = {}
	def activate(self, window):
		self._instances[window] = HilightPyWindowHelper(self, window)
	def deactivate(self, window):
		self._instances[window].deactivate()
		del self._instances[window]
	def update_ui(self, window):
		self._instances[window].update_ui()
