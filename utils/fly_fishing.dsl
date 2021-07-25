TABLE trout_outings {
    trout_outing_id SERIAL [pk]
    outing_date DATE
    location VARCHAR(512)
    weather VARCHAR(64)
    description VARCHAR(512)
    brown INT
    brook INT
    rainbow INT
    tiger INT
    other INT
}

TABLE hook_lengths {
    hook_length_id SERIAL [pk]
    length VARCHAR(4)
    description VARCHAR(32)
  //PRIMARY KEY (hook_length_id)
  //CONSTRAINT uc_hook_length_name UNIQUE (length)
}

TABLE hook_weights {
    hook_weight_id SERIAL [pk]
    weight VARCHAR(4)
    description VARCHAR(32)
  //PRIMARY KEY (hook_weight_id)
  //CONSTRAINT uc_hook_weight_name UNIQUE (weight)
}

TABLE eye_types {
    eye_type_id SERIAL [pk]
    type VARCHAR(16)
    description VARCHAR(512)
  //PRIMARY KEY (eye_type_id)
  //CONSTRAINT uc_eye_type UNIQUE (type) 
}

TABLE hook_types {
    hook_type_id SERIAL [pk]
    type VARCHAR(16)
    description VARCHAR(512)
  //PRIMARY KEY (hook_type_id)
  //CONSTRAINT uc_hook_type UNIQUE (type) 
}

TABLE bend_types {
    bend_type_id SERIAL [pk]
    type VARCHAR(16)
    description VARCHAR(512)
  //PRIMARY KEY (bend_type_id)
  //CONSTRAINT uc_bend_type UNIQUE (type) 
}

TABLE shank_types {
    shank_type_id SERIAL [pk]
    type VARCHAR(16)
    description VARCHAR(512)
  //PRIMARY KEY (shank_type_id)
  //CONSTRAINT uc_shank_type UNIQUE (type) 
}

TABLE hooks {
    hook_id SERIAL [pk]
    brand VARCHAR(16)
    model VARCHAR(16)
    length VARCHAR(4)
    weight VARCHAR(4)
    eye_type VARCHAR(16)
    hook_type VARCHAR(16)
    bend_type VARCHAR(16)
    shank_type VARCHAR(16)
    barbless BOOLEAN
  //PRIMARY KEY (hook_id)
  //CONSTRAINT fk_hook_length
    //FOREIGN KEY (length)
      //REFERENCES hook_lengths (length)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_hook_weights
    //FOREIGN KEY (weight)
      //REFERENCES hook_weights (weight)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_eye_type
    //FOREIGN KEY (eye_type)
      //REFERENCES eye_types (type)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_hook_type
    //FOREIGN KEY (hook_type)
      //REFERENCES hook_types (type)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_bend_type
    //FOREIGN KEY (bend_type)
      //REFERENCES bend_types (type)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_shank_type
    //FOREIGN KEY (shank_type)
      //REFERENCES shank_types (type)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE        
}

TABLE units_names {
    units_name_id SERIAL [pk]
    units VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (units_name_id)
  //CONSTRAINT uc_units_name UNIQUE (units)
}

TABLE hole_types {
    hole_type_id SERIAL [pk]
    type VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (hole_type_id)
  //CONSTRAINT uc_bead_hole_type UNIQUE (type)
}

TABLE bead_shapes {
    bead_shape_id SERIAL [pk]
    shape VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (bead_shape_id)
  //CONSTRAINT uc_bead_shape_type UNIQUE (shape)
}

TABLE bead_material_types {
    bead_material_id SERIAL [pk]
    material VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (bead_material_id)
  //CONSTRAINT uc_bead_material_type UNIQUE (material)
}

TABLE beads {
    bead_id SERIAL [pk]
    size VARCHAR(8)
    units VARCHAR(16)
    shape VARCHAR(16)
    color VARCHAR(16)
    material VARCHAR(16)
    hole_type VARCHAR(16)
  //PRIMARY KEY (bead_id)
  //CONSTRAINT fk_units_type
    //FOREIGN KEY (units)
      //REFERENCES units_names(units)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_hole_type
    //FOREIGN KEY (hole_type)
      //REFERENCES hole_types(type)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_bead_shape
    //FOREIGN KEY (shape)
      //REFERENCES bead_shapes(shape)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_material_type
    //FOREIGN KEY (material)
      //REFERENCES bead_material_types(material)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
}

TABLE bead_to_hook {
    bead_to_hook_id SERIAL [pk]
    baed_id INT    
    bead_size VARCHAR(8)
    hook_size INT
  //PRIMARY KEY (bead_to_hook_id)
}

TABLE thread_material_types {
    thread_material_id SERIAL [pk]
    material VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (thread_material_id)
  //CONSTRAINT uc_thread_material UNIQUE (material)
}

TABLE thread_twist_types {
    thread_twist_id SERIAL [pk]
    twist VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (thread_twist_id)
  //CONSTRAINT uc_thread_twist UNIQUE (twist)
}

TABLE thread_sizes {
   thread_size_id SERIAL [pk]
    size VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (thread_size_id)
  //CONSTRAINT uc_thread_size UNIQUE (size)
}

TABLE thread {
    thread_id SERIAL [pk]
    brand VARCHAR(16)
    color VARCHAR(16)
    material VARCHAR(16)
    size VARCHAR(4)
    waxed BOOLEAN
    twist VARCHAR(16) 
    strength INT
  //PRIMARY KEY (thread_id)
  //CONSTRAINT fk_thread_material
    //FOREIGN KEY (material)
      //REFERENCES thread_material_types(material)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_thread_twist
    //FOREIGN KEY (twist)
      //REFERENCES thread_twist_types(twist)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_thread_size
    //FOREIGN KEY (size)
      //REFERENCES thread_sizes(size)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
}

TABLE wire_materials {
    wire_material_id SERIAL [pk]
    material VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (wire_material_id)
  //CONSTRAINT uc_wire_material UNIQUE (material)
}

TABLE wire_sizes {
    wire_size_id SERIAL [pk]
    size VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (wire_size_id)
  //CONSTRAINT uc_wire_size UNIQUE (size)
}

TABLE wire {
    wire_id SERIAL [pk]
    brand VARCHAR(16)
    color VARCHAR(16)
    material VARCHAR(16)
    size VARCHAR(4)
  //PRIMARY KEY (wire_id)
  //CONSTRAINT fk_wire_material
    //FOREIGN KEY (material)
      //REFERENCES wire_materials(material)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
  //CONSTRAINT fk_wire_size
    //FOREIGN KEY (size)
      //REFERENCES wire_sizes(size)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
}

TABLE dubbing_materials {
    dubbing_material_id SERIAL [pk]
    material VARCHAR(16)
    description VARCHAR(128)
  //PRIMARY KEY (dubbing_material_id)
  //CONSTRAINT uc_dubbing_material UNIQUE (material)
}

TABLE dubbing {
    dubbing_id SERIAL [pk]
    brand VARCHAR(16)
    color VARCHAR(16)
    material VARCHAR(16)
  //PRIMARY KEY (dubbing_id)
  //CONSTRAINT fk_dubbing_material
    //FOREIGN KEY (material)
      //REFERENCES wire_materials(material)
      //ON DELETE RESTRICT
      //ON UPDATE CASCADE
}
