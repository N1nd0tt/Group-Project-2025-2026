package com.example.projekt_zesp.controller;

import com.example.projekt_zesp.models.History;
import com.example.projekt_zesp.service.HistoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/histories")
public class HistoryController {

    @Autowired
    private HistoryService historyService;

    @PostMapping
    public ResponseEntity<History> saveHistory(@RequestBody History history) {
        return ResponseEntity.ok(historyService.saveHistory(history));
    }

    @GetMapping("/owner/{owner}")
    public ResponseEntity<List<History>> getHistoriesByOwner(@PathVariable String owner) {
        return ResponseEntity.ok(historyService.getHistoriesByOwner(owner));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteHistory(@PathVariable Long id) {
        historyService.deleteHistory(id);
        return ResponseEntity.noContent().build();
    }
}
