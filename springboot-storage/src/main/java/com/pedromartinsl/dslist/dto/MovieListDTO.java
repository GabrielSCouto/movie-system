package com.pedromartinsl.dslist.dto;

import com.pedromartinsl.dslist.entities.MovieList;

public class MovieListDTO {
    private final Long id;
	private final String name;
	
	public MovieListDTO(MovieList entity) {
		id = entity.getId();
		name = entity.getName();
	}
	public Long getId() {
		return id;
	}
	public String getName() {
		return name;
	}
}
