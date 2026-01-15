package com.example.projekt_zesp.service.impl;

import com.example.projekt_zesp.models.History;
import com.example.projekt_zesp.repository.HistoryRepository;
import com.example.projekt_zesp.service.HistoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class HistoryServiceImpl implements HistoryService {
    @Autowired
    private HistoryRepository historyRepository;

    @Override
    public History saveHistory(History history) {
        return historyRepository.save(history);
    }

    @Override
    public List<History> getHistoriesByOwner(String owner) {
        return historyRepository.findByOwner(owner);
    }

    @Override
    public void deleteHistory(Long id) {
        historyRepository.deleteById(id);
    }
}
