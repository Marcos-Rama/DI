package com.example.mycatalog;

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
        setContentView(R.layout.activity_detail);
        ImageView imageView = findViewById(R.id.Imagen1);

        // Carga la imagen usando Picasso con la transformación circular
        Picasso.get()
                .load(R.drawable.carta5) // También puedes usar una URL
                .transform(new CircleTransform())
                .into(imageView);
    }
}