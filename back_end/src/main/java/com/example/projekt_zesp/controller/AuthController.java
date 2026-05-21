package com.example.projekt_zesp.controller;

import com.example.projekt_zesp.service.AuthService;
import com.example.projekt_zesp.service.JwtService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
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
        
        var dbUser = authService.findByLogin(login);
        
        UserDetails userDetails = User.builder()
                .username(dbUser.getLogin())
                .password(dbUser.getPassword())
                .roles("USER")
                .build();

        String jwtToken = jwtService.generateToken(userDetails);
        
        return ResponseEntity.ok(jwtToken);
    }
}