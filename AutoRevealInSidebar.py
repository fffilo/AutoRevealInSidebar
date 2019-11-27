import sublime
import sublime_plugin

class AutoRevealInSidebarListener(sublime_plugin.EventListener):

    def on_activated(self, view):
        window = view.window();
        visible = window.is_sidebar_visible()
        settings = sublime.load_settings("AutoRevealInSidebar.sublime-settings")
        active = settings.get("plugin_enabled", True)
        force = settings.get("force_open_sidebar", False)

        if (not active):
            return
        if (not visible and not force):
            return

        window.run_command("reveal_in_side_bar")
