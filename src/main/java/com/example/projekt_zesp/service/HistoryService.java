package com.example.projekt_zesp.service;

import com.example.projekt_zesp.models.History;

import java.util.List;

public interface HistoryService {
    History saveHistory(History history);
    List<History> getHistoriesByOwner(String owner);
    void deleteHistory(Long id);
}
