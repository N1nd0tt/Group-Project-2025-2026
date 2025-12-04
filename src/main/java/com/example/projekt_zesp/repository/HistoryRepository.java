package com.example.projekt_zesp.repository;

import com.example.projekt_zesp.models.History;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface HistoryRepository extends JpaRepository<History, Long> {
    List<History> findByOwner(String owner);
}
