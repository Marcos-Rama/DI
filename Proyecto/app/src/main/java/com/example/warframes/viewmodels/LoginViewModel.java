package com.example.warframes.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.warframes.repositories.UserRepository;

public class LoginViewModel extends ViewModel {
    private final UserRepository repository;
    private final MutableLiveData<String> errorMessage = new MutableLiveData<>();
    private final MutableLiveData<Boolean> loginSuccess = new MutableLiveData<>();
    private final MutableLiveData<Boolean> isLoading = new MutableLiveData<>();
    private final MutableLiveData<Void> navigateToDashboard = new MutableLiveData<>();
    public LoginViewModel() {
        repository = new UserRepository();
    }
    public LiveData<String> getErrorMessage() { return errorMessage; }
    public LiveData<Boolean> getIsLoading() { return isLoading; }
    public LiveData<Boolean> getLoginSuccess() { return loginSuccess; }
    public LiveData<Void> getNavigateToDashboard() { return navigateToDashboard; }

    public void loginUser(String email, String password) {

        if (email.isEmpty() || password.isEmpty()) {
            errorMessage.setValue("Todos los campos son obligatorios");
            return;
        }
        isLoading.setValue(true);

        repository.loginUser(email, password)
                .addOnSuccessListener(authResult -> {
                    loginSuccess.setValue(true);
                    isLoading.setValue(false);
                    navigateToDashboard.setValue(null);

                })
                .addOnFailureListener(e -> {
                    errorMessage.setValue("Error en el registro: " + e.getMessage());
                    isLoading.setValue(false);
                });
    }

}
