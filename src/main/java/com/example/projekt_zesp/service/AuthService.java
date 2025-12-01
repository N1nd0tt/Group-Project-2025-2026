package com.example.projekt_zesp.service;

import com.example.projekt_zesp.models.User;
import com.example.projekt_zesp.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import java.util.UUID;

@Service
@RequiredArgsConstructor
public class AuthService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public void register(String login, String rawPassword) {
        if (userRepository.findByLogin(login).isPresent()) {
            throw new RuntimeException("User already exists");
        }

        var user = User.builder()
            .id(UUID.randomUUID().toString())
            .login(login)
            .password(passwordEncoder.encode(rawPassword))
            .build();

        userRepository.save(user);
    }

    public User findByLogin(String login) {
        return userRepository.findByLogin(login)
                .orElseThrow(() -> new RuntimeException("User not found"));
    }
}