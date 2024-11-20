package com.example.mycatalog;

import android.content.res.Configuration;
import android.os.Bundle;
import android.widget.ImageView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import com.squareup.picasso.Picasso;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);

        int orientation = getResources().getConfiguration().orientation;
        // Cambiar el layout según la orientación
        if (orientation == Configuration.ORIENTATION_LANDSCAPE) {
            // Si está en horizontal (landscape), usa un layout horizontal
            setContentView(R.layout.detail_activity);
        } else {
            // Si está en vertical (portrait), usa el layout por defecto
            setContentView(R.layout.activity_detail);
        }

        ImageView imageView = findViewById(R.id.Imagen1);

        // Carga la imagen usando Picasso con la transformación circular
        Picasso.get()
                .load(R.drawable.carta5) // También puedes usar una URL
                .transform(new CircleTransform())
                .into(imageView);
    }
}