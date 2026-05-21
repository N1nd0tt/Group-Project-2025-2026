package com.example.projekt_zesp.models;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "histories")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class History {
    @Id
    @Column(nullable = false, unique = true)
    private String campaignId;

    @Column(nullable = false)
    private String ownerId;

    @Column(nullable = false)
    private String status;

    @Column(nullable = false)
    private String details;
}