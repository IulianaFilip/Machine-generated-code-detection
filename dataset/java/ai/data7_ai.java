package com.example.rest_service;

import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Data7 {

    private static final String TEMPLATE = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong(0);

    @GetMapping("/greeting")
    public Greeting greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
        long id = counter.incrementAndGet();
        String message = String.format(TEMPLATE, name);
        return new Greeting(id, message);
    }
}
