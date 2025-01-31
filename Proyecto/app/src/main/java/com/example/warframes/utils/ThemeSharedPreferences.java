package com.example.warframes.utils;

import android.content.Context;
import android.content.SharedPreferences;

import com.example.warframes.R;

public class ThemeSharedPreferences {
    private static final String PREF_NAME = "theme_preferences";
    private static final String KEY_THEME_MODE = "theme_mode";

    private final SharedPreferences sharedPreferences;

    public ThemeSharedPreferences(Context context) {
        sharedPreferences = context.getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE);
    }

    // Guardar el estado
    public void setDarkModeEnabled(boolean isDarkMode) {
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putBoolean(KEY_THEME_MODE, isDarkMode);
        editor.apply();
    }

    // Obtener el estado
    public boolean isDarkModeEnabled() {
        return sharedPreferences.getBoolean(KEY_THEME_MODE, false); // Valor por defecto (tema claro)
    }


}