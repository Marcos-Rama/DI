package com.example.warframes.views;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.example.warframes.R;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;


public class DashboardActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    private Context context = this;
    private DatabaseReference databaseRef;
    // Referencias a los componentes de la interfaz de usuario: un ImageView y dos TextViews.
    private ImageView imageView;
    private TextView titleTextView, descriptionTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        // Inicializamos las vistas desde el layout XML.
        titleTextView = findViewById(R.id.titleTextView);
        descriptionTextView = findViewById(R.id.descriptionTextView);
        imageView = findViewById(R.id.imageView);

        Button logOutButton = findViewById(R.id.logOutButton);
        mAuth = FirebaseAuth.getInstance();

        // Inicializamos DatabaseReference para poder leer los datos de Firebase de un objeto concreto de momento.
        databaseRef = FirebaseDatabase.getInstance().getReference().child("warframes/002");;

        logOutButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(context, LoginActivity.class);
                context.startActivity(myIntent);
            }
        });

        // Configuramos un listener para obtener datos en tiempo real de la base de datos.
        databaseRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                //  Se ejecuta cuando se obtienen datos de la base de datos. Los datos se devuelven como un objeto DataSnapshot
                if (dataSnapshot.exists()) {
                    // Obtenemos los valores de "name", "description" e "image" desde la base de datos.
                    String title = dataSnapshot.child("name").getValue(String.class);
                    String description = dataSnapshot.child("description").getValue(String.class);
                    String imageUrl = dataSnapshot.child("image").getValue(String.class);

                    // Actualizamos la interfaz de usuario con los datos obtenidos.
                    titleTextView.setText(title);
                    descriptionTextView.setText(description);
                    // Usamos Glide para cargar la imagen desde la URL proporcionada en la base de datos.
                    Glide.with(context).load(imageUrl).into(imageView);
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Toast.makeText(context, "Error al cargar datos", Toast.LENGTH_SHORT).show();
            }
        });


    }
}