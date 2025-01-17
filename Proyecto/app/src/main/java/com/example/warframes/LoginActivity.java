package com.example.warframes;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import android.content.Context;

import androidx.appcompat.app.AppCompatActivity;
import com.google.firebase.auth.FirebaseAuth;


public class LoginActivity extends AppCompatActivity {
    private Context context = this;
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        mAuth = FirebaseAuth.getInstance();

        Button registerButton = findViewById(R.id.registerButton);
        findViewById(R.id.loginButton).setOnClickListener(v -> loginUser());
        registerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(context, RegisterActivity.class);
                context.startActivity(myIntent);
            }
        });
    }
        private void loginUser() {
            String email = ((EditText) findViewById(R.id.emailEditText)).getText().toString();
            String password = ((EditText) findViewById(R.id.passwordEditText)).getText().toString();

            if  (email.isEmpty() || password.isEmpty()) {
                Toast.makeText(context, "Email o contraseña vacíos", Toast.LENGTH_SHORT).show();
                return;
            }
            mAuth.signInWithEmailAndPassword(email, password)
                    .addOnCompleteListener(this, task -> {
                        if (task.isSuccessful()) {
                            Toast.makeText(context, "Inicio de sesión exitoso.", Toast.LENGTH_SHORT).show();
                            Intent myIntent = new Intent(context, DashboardActivity.class);
                            context.startActivity(myIntent);
                        } else {
                            Toast.makeText(context, "Error en autenticación.", Toast.LENGTH_SHORT).show();
                        }
                    });
        }


}