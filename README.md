# Fullbright & NoFog (Horizon native mod)

Toggle full brightness and the world's fog in Horizon 26.3.

| Toggle | Key (rebindable) | Command |
| --- | --- | --- |
| Fullbright (gamma 1500%) | G | `/fullbright [on\|off]` (or `/fb`) |
| NoFog | N | `/nofog [on\|off]` |
| NoFog also in water / lava / powder snow | – | `/nofog fluids` |

Options > Mods > Fullbright & NoFog has a button for each toggle and the two keys.
Settings persist in `horizon-mods/.horizon-mod-data/fullbright_nofog/`. Your brightness
slider and `options.txt` are never touched; turning Fullbright off restores your slider.
Toggling is silent (no chat messages). Client-side only: works in single player and on servers.

## Install

1. Download `fullbright_nofog-1.0.0.hnmod` from [Releases](https://github.com/Nirokx/horizon-fullbright-nofog/releases),
   then Launcher > Mods > add a native mod from file (or build it yourself with `python3 pack.py`).
2. Press **Build** (native mods are compiled into a game of their own; read the source first).

## Rebuild the package

```sh
python3 pack.py
cargo test   # runtime logic tests
```

Hooks used: `native_frame`, `native_render_fog`, `native_command`, `native_key`,
`native_mods`, `native_settings`, `native_settings_click` (needs Horizon native hooks API 80+,
made against Nightly 2026-11-01 `c9d474d`).

## License

MIT, see [LICENSE](LICENSE).
