DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM pg_trigger
    WHERE tgname = 'updated_at_location_trigger'
) THEN CREATE TRIGGER updated_at_location_trigger BEFORE
    UPDATE ON location FOR EACH ROW EXECUTE FUNCTION update_updated_at();
END IF;
END $$;