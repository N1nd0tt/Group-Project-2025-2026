package com.example.projekt_zesp.controller;

import com.example.projekt_zesp.models.Game;
import com.example.projekt_zesp.models.User;
import com.example.projekt_zesp.service.GameService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/games")
public class GameController {

    @Autowired
    private GameService gameService;

    @PostMapping
    public ResponseEntity<Game> createGame(@RequestBody Game game) {
        Game createdGame = gameService.createGame(game);
        return ResponseEntity.ok(createdGame);
    }

    @PostMapping("/{gameId}/players")
    public ResponseEntity<Game> addPlayerToGame(@PathVariable String gameId, @RequestBody User player) {
    Game updatedGame = gameService.addPlayerToGame(gameId, player);
        return ResponseEntity.ok(updatedGame);
    }

    @DeleteMapping("/{gameId}/players/{playerId}")
    public ResponseEntity<Game> removePlayerFromGame(@PathVariable String gameId, @PathVariable String playerId) {
        Game updatedGame = gameService.removePlayerFromGame(gameId, playerId);
        return ResponseEntity.ok(updatedGame);
    }

    @DeleteMapping("/{gameId}")
    public ResponseEntity<Void> removeGame(@PathVariable String gameId) {
        gameService.removeGame(gameId);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/{gameId}")
    public ResponseEntity<Game> getGameInfo(@PathVariable String gameId) {
        Game game = gameService.getGameInfo(gameId);
        return ResponseEntity.ok(game);
    }

    @GetMapping("/owner/{owner}")
    public ResponseEntity<List<Game>> getAllGamesByOwner(@PathVariable String owner) {
        List<Game> games = gameService.getAllGamesByOwner(owner);
        return ResponseEntity.ok(games);
    }
}
