        CREATE TABLE IF NOT EXISTS trout_outings (
            trout_outing_id SERIAL NOT NULL,
            outing_date DATE NOT NULL,
            location VARCHAR(512) NOT NULL,
            weather VARCHAR(64) NOT NULL,
            description VARCHAR(512),
            brown INT NOT NULL DEFAULT 0,
            brook INT NOT NULL DEFAULT 0,
            rainbow INT NOT NULL DEFAULT 0,
            tiger INT NOT NULL DEFAULT 0,
            other INT NOT NULL DEFAULT 0,
            PRIMARY KEY (trout_outing_id)
        );

        CREATE TABLE IF NOT EXISTS hook_lengths (
            hook_length_id SERIAL NOT NULL,
            length VARCHAR(4) NOT NULL,
            description VARCHAR(32),
          PRIMARY KEY (hook_length_id),
          CONSTRAINT uc_hook_length_name UNIQUE (length)
        );
 
        CREATE TABLE IF NOT EXISTS hook_weights (
            hook_weight_id SERIAL NOT NULL,
            weight VARCHAR(4) NOT NULL,
            description VARCHAR(32),
          PRIMARY KEY (hook_weight_id),
          CONSTRAINT uc_hook_weight_name UNIQUE (weight)
        );

        CREATE TABLE IF NOT EXISTS eye_types (
            eye_type_id SERIAL NOT NULL,
            type VARCHAR(16) NOT NULL,
            description VARCHAR(512),
          PRIMARY KEY (eye_type_id),
          CONSTRAINT uc_eye_type UNIQUE (type) 
        );

        CREATE TABLE IF NOT EXISTS hook_types (
            hook_type_id SERIAL NOT NULL,
            type VARCHAR(16) NOT NULL,
            description VARCHAR(512),
          PRIMARY KEY (hook_type_id),
          CONSTRAINT uc_hook_type UNIQUE (type) 
        );

        CREATE TABLE IF NOT EXISTS bend_types (
            bend_type_id SERIAL NOT NULL,
            type VARCHAR(16) NOT NULL,
            description VARCHAR(512),
          PRIMARY KEY (bend_type_id),
          CONSTRAINT uc_bend_type UNIQUE (type) 
        );

        CREATE TABLE IF NOT EXISTS shank_types (
            shank_type_id SERIAL NOT NULL,
            type VARCHAR(16) NOT NULL,
            description VARCHAR(512),
          PRIMARY KEY (shank_type_id),
          CONSTRAINT uc_shank_type UNIQUE (type) 
        );

        CREATE TABLE IF NOT EXISTS hooks (
            hook_id SERIAL NOT NULL,
            brand VARCHAR(16) NOT NULL,
            model VARCHAR(16) NOT NULL,
            length VARCHAR(4) NOT NULL DEFAULT 0X,
            weight VARCHAR(4) NOT NULL DEFAULT 0X,
            eye_type VARCHAR(16) NOT NULL,
            hook_type VARCHAR(16) NOT NULL,
            bend_type VARCHAR(16) NOT NULL,
            shank_type VARCHAR(16) NOT NULL,
            barbless BOOLEAN DEFAULT f,
          PRIMARY KEY (hook_id),
          CONSTRAINT fk_hook_length
            FOREIGN KEY (length)
              REFERENCES hook_lengths (length)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_hook_weights
            FOREIGN KEY (weight)
              REFERENCES hook_weights (weight)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_eye_type
            FOREIGN KEY (eye_type)
              REFERENCES eye_types (type)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_hook_type
            FOREIGN KEY (hook_type)
              REFERENCES hook_types (type)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_bend_type
            FOREIGN KEY (bend_type)
              REFERENCES bend_types (type)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_shank_type
            FOREIGN KEY (shank_type)
              REFERENCES shank_types (type)
              ON DELETE RESTRICT
              ON UPDATE CASCADE        
        );

        CREATE TABLE IF NOT EXISTS units_names (
            units_name_id SERIAL NOT NULL,
            units VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (units_name_id),
          CONSTRAINT uc_units_name UNIQUE (units)
        );

        CREATE TABLE IF NOT EXISTS hole_types (
            hole_type_id SERIAL NOT NULL,
            type VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (hole_type_id),
          CONSTRAINT uc_bead_hole_type UNIQUE (type)
        );

        CREATE TABLE IF NOT EXISTS bead_shapes (
            bead_shape_id SERIAL NOT NULL,
            shape VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (bead_shape_id),
          CONSTRAINT uc_bead_shape_type UNIQUE (shape)
        );

        CREATE TABLE IF NOT EXISTS bead_material_types (
            bead_material_id SERIAL NOT NULL,
            material VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (bead_material_id),
          CONSTRAINT uc_bead_material_type UNIQUE (material)
        );

        CREATE TABLE IF NOT EXISTS beads (
            bead_id SERIAL NOT NULL,
            size VARCHAR(8) NOT NULL,
            units VARCHAR(16) NOT NULL,
            shape VARCHAR(16) NOT NULL,
            color VARCHAR(16) NOT NULL,
            material VARCHAR(16) NOT NULL,
            hole_type VARCHAR(16) NOT NULL,
          PRIMARY KEY (bead_id),
          CONSTRAINT fk_units_type
            FOREIGN KEY (units)
              REFERENCES units_names(units)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_hole_type
            FOREIGN KEY (hole_type)
              REFERENCES hole_types(type)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_bead_shape
            FOREIGN KEY (shape)
              REFERENCES bead_shapes(shape)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_material_type
            FOREIGN KEY (material)
              REFERENCES bead_material_types(material)
              ON DELETE RESTRICT
              ON UPDATE CASCADE
        );

        CREATE TABLE IF NOT EXISTS bead_to_hook (
            bead_to_hook_id SERIAL NOT NULL,
            baed_id INT NOT NULL,    
            bead_size VARCHAR(8) NOT NULL,
            hook_size INT NOT NULL,
          PRIMARY KEY (bead_to_hook_id)
        );

        CREATE TABLE IF NOT EXISTS thread_material_types (
            thread_material_id SERIAL NOT NULL,
            material VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (thread_material_id),
          CONSTRAINT uc_thread_material UNIQUE (material)
        );

        CREATE TABLE IF NOT EXISTS thread_twist_types (
            thread_twist_id SERIAL NOT NULL,
            twist VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (thread_twist_id),
          CONSTRAINT uc_thread_twist UNIQUE (twist)
        );

        CREATE TABLE IF NOT EXISTS thread_sizes (
           thread_size_id SERIAL NOT NULL,
            size VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (thread_size_id),
          CONSTRAINT uc_thread_size UNIQUE (size)
        );

        CREATE TABLE IF NOT EXISTS thread (
            thread_id SERIAL NOT NULL,
            brand VARCHAR(16) NOT NULL,
            color VARCHAR(16) NOT NULL,
            material VARCHAR(16) NOT NULL,
            size VARCHAR(4) NOT NULL,
            waxed BOOLEAN NOT NULL DEFAULT f,
            twist VARCHAR(16) NOT NULL, 
            strength INT,
          PRIMARY KEY (thread_id),
          CONSTRAINT fk_thread_material
            FOREIGN KEY (material)
              REFERENCES thread_material_types(material)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_thread_twist
            FOREIGN KEY (twist)
              REFERENCES thread_twist_types(twist)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_thread_size
            FOREIGN KEY (size)
              REFERENCES thread_sizes(size)
              ON DELETE RESTRICT
              ON UPDATE CASCADE
        );

        CREATE TABLE IF NOT EXISTS wire_materials (
            wire_material_id SERIAL NOT NULL,
            material VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (wire_material_id),
          CONSTRAINT uc_wire_material UNIQUE (material)
        );

        CREATE TABLE IF NOT EXISTS wire_sizes (
            wire_size_id SERIAL NOT NULL,
            size VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (wire_size_id),
          CONSTRAINT uc_wire_size UNIQUE (size)
        );

        CREATE TABLE IF NOT EXISTS wire (
            wire_id SERIAL NOT NULL,
            brand VARCHAR(16) NOT NULL,
            color VARCHAR(16) NOT NULL,
            material VARCHAR(16) NOT NULL,
            size VARCHAR(4) NOT NULL,
          PRIMARY KEY (wire_id),
          CONSTRAINT fk_wire_material
            FOREIGN KEY (material)
              REFERENCES wire_materials(material)
              ON DELETE RESTRICT
              ON UPDATE CASCADE,
          CONSTRAINT fk_wire_size
            FOREIGN KEY (size)
              REFERENCES wire_sizes(size)
              ON DELETE RESTRICT
              ON UPDATE CASCADE
        );

        CREATE TABLE IF NOT EXISTS dubbing_materials (
            dubbing_material_id SERIAL NOT NULL,
            material VARCHAR(16) NOT NULL,
            description VARCHAR(128),
          PRIMARY KEY (dubbing_material_id),
          CONSTRAINT uc_dubbing_material UNIQUE (material)
        );

        CREATE TABLE IF NOT EXISTS dubbing (
            dubbing_id SERIAL NOT NULL,
            brand VARCHAR(16) NOT NULL,
            color VARCHAR(16) NOT NULL,
            material VARCHAR(16) NOT NULL,
          PRIMARY KEY (dubbing_id),
          CONSTRAINT fk_dubbing_material
            FOREIGN KEY (material)
              REFERENCES dubbing_materials(material)
              ON DELETE RESTRICT
              ON UPDATE CASCADE
        );
