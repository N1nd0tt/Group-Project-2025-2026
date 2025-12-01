package com.example.projekt_zesp.controllers;

import com.example.projekt_zesp.services.AuthService;
import com.example.projekt_zesp.services.JwtService;

import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
@RequiredArgsConstructor
public class AuthController {

    private final AuthService authService;
    private final AuthenticationManager authenticationManager; 
    private final JwtService jwtService;

    @PostMapping("/register")
    public ResponseEntity<String> register(@RequestParam String login, @RequestParam String password) {
        authService.register(login, password);
        return ResponseEntity.ok("User created successfully!");
    }

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestParam String login, @RequestParam String password) {
        authenticationManager.authenticate(
            new UsernamePasswordAuthenticationToken(login, password)
        );
        
        var user = authService.findByLogin(login);
        
        var userDetails = org.springframework.security.core.userdetails.User.builder()
                .username(login)
                .password(password)
                .roles("USER")
                .build();

        String jwtToken = jwtService.generateToken(userDetails);
        
        return ResponseEntity.ok(jwtToken);
    }
}