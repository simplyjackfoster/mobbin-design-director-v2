import importlib.util
import io
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/mobbin-design-director/scripts'


def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


lint = module('swiftui_slop_lint')

SLOPPY = '''import SwiftUI

struct HeroView: View {
    var body: some View {
        VStack {
            Text("Welcome to App \U0001F680")
                .font(.system(size: 34))
                .fontWeight(.bold)
            Text("Lorem ipsum dolor")
                .fontWeight(.semibold)
                .padding(13)
                .padding(.horizontal, 16)
            Image(systemName: "line.3.horizontal")
            Image(systemName: "star")
                .onTapGesture { print("tap") }
        }
        .background(LinearGradient(colors: [.purple, .blue],
                                   startPoint: .top, endPoint: .bottom))
        .foregroundColor(Color.purple)
        .cornerRadius(16)
        .shadow(radius: 8)
    }
}
'''

CLEAN = '''import SwiftUI

struct RowView: View {
    var body: some View {
        Button(action: {}) {
            Label("Open", systemImage: "arrow.right")
        }
        .padding(16)
        Image(systemName: "star").accessibilityLabel("Favourite")
        Button { } label: { Text("Save") }
            .onTapGesture { }
    }
}
'''


class SlopLintTests(unittest.TestCase):
    def test_counts_every_tell_in_the_sloppy_fixture(self):
        hits = lint.scan_lines(SLOPPY.splitlines(keepends=True))
        self.assertEqual(hits['gradient_purple_blue'], [17])
        self.assertEqual(hits['fixed_font_size'], [7])
        self.assertEqual(hits['font_weight'], [8, 10])
        self.assertEqual(hits['tap_gesture_not_button'], [15])
        self.assertEqual(hits['color_purple'], [19])
        self.assertEqual(hits['emoji_in_text'], [6])
        self.assertEqual(hits['symbol_without_label'], [13, 14])
        self.assertEqual(hits['corner_radius_with_shadow'], [20])
        self.assertEqual(hits['lorem'], [9])
        self.assertEqual(hits['padding_off_grid'], [11])
        self.assertEqual(hits['hamburger_symbol'], [13])

    def test_clean_fixture_has_no_hits(self):
        hits = lint.scan_lines(CLEAN.splitlines(keepends=True))
        self.assertEqual({key: lines for key, lines in hits.items() if lines}, {})

    def test_cli_scans_a_tree_and_always_exits_zero(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'Views').mkdir()
            (root / 'Views/Hero.swift').write_text(SLOPPY)
            (root / 'Row.swift').write_text(CLEAN)
            (root / 'notes.txt').write_text('LinearGradient .purple')
            out = io.StringIO()
            with redirect_stdout(out):
                code = lint.main([str(root), '--limit', '1'])
            text = out.getvalue()
            self.assertEqual(code, 0)
            self.assertIn('Views/Hero.swift:17', text)
            self.assertIn('... 1 more', text)
            self.assertIn('fixed_font_size', text)
            self.assertTrue(text.rstrip().endswith('Counts are diagnostics, not verdicts.'))
            with redirect_stdout(io.StringIO()):
                self.assertEqual(lint.main([str(root / 'missing')]), 0)


if __name__ == '__main__':
    unittest.main()
