package com.example.warframes.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.warframes.models.Warframe;
import com.example.warframes.repositories.DashboardRepository;

import java.util.List;

public class DashboardViewModel extends ViewModel {

    private final MutableLiveData<List<Warframe>> warframeLiveData = new MutableLiveData<>();
    private final DashboardRepository warframeRepository;

    public DashboardViewModel() {
        warframeRepository = new DashboardRepository();
        loadWarframes();
    }

    public LiveData<List<Warframe>> getWarframeLiveData() {
        return warframeLiveData;
    }

    private void loadWarframes() {
        warframeRepository.getWarframes(warframeLiveData);
    }
}