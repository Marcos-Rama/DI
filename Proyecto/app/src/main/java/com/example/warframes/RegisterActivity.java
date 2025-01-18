package com.example.warframes;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.EditText;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;


import androidx.appcompat.app.AppCompatActivity;

import java.util.HashMap;
import java.util.Map;


public class RegisterActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    private Context context = this;
    private DatabaseReference databaseRef;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        findViewById(R.id.registerButton).setOnClickListener(v -> registerUser());

        mAuth = FirebaseAuth.getInstance();
        databaseRef = FirebaseDatabase.getInstance().getReference();

    }
    private void registerUser() {
        String name = ((EditText) findViewById(R.id.nameEditText)).getText().toString();
        String email = ((EditText) findViewById(R.id.emailRegisterEditText)).getText().toString();
        String password = ((EditText) findViewById(R.id.passwordRegisterEditText)).getText().toString();
        String repassword = ((EditText) findViewById(R.id.passwordConfirmRegisterEditText)).getText().toString();
        String telephone = ((EditText) findViewById(R.id.telephoneEditText)).getText().toString();
        String address = ((EditText) findViewById(R.id.addressEditText)).getText().toString();

        if ((name.isEmpty() || email.isEmpty() || password.isEmpty() || repassword.isEmpty() ||
                telephone.isEmpty() || address.isEmpty())) {
            Toast.makeText(context, "Algún campo vacío", Toast.LENGTH_SHORT).show();
            return;
        }
        if (!password.equals(repassword)) {
            Toast.makeText(context, "Constraseñas distintas", Toast.LENGTH_SHORT).show();
            return;
        }
            mAuth.createUserWithEmailAndPassword(email, password)
                    .addOnCompleteListener(this, task -> {
                        if (task.isSuccessful()) {
                            Toast.makeText(context, "Task successful??", Toast.LENGTH_SHORT).show();
                            FirebaseUser firebaseUser = task.getResult().getUser();

                            Toast.makeText(context, "mAuth.getCurrent", Toast.LENGTH_SHORT).show();

                            if (firebaseUser != null) {
                                String uid = firebaseUser.getUid();
                                Toast.makeText(context, "UID obtenido: " + uid, Toast.LENGTH_SHORT).show();
                                Map<String, Object> newUser = new HashMap<>();
                                newUser.put("name", name);
                                newUser.put("email", email);
                                newUser.put("telephone", telephone);
                                newUser.put("address", address);
                                Toast.makeText(context, "control3", Toast.LENGTH_SHORT).show();//Este se muestra
                                databaseRef.child("users").child(uid).setValue(newUser)
                                        .addOnCompleteListener(dbTask -> {
                                            if (dbTask.isSuccessful()) {
                                                Toast.makeText(RegisterActivity.this, "Registro exitoso.", Toast.LENGTH_SHORT).show();
                                                startActivity(new Intent(RegisterActivity.this, LoginActivity.class));
                                                finish();
                                            } else {
                                                Toast.makeText(RegisterActivity.this, "Error al guardar datos.", Toast.LENGTH_SHORT).show();
                                            }
                                        });
                            }
                        } else {
                            Toast.makeText(context, "Error en el registro", Toast.LENGTH_LONG).show();
                            Log.e("Firebase", "Error al registrar usuario", task.getException());
                        }
                    });

        }

        public static class User {
            public String uid;
            public String name;
            public String email;
            public String telephone;
            public String address;


            // Constructor vacío necesario para Firebase
            public User() {
            }

            public User(String uid, String name,String email, String telephone, String address) {
                this.uid = uid;
                this.name = name;
                this.email = email;
                this.telephone = telephone;
                this.address = address;
            }
        }
    }
