package com.example.art_gal.config;
import java.sql.Connection;
import java.sql.DriverManager;

public class Mysql {
    public static void main(String[] args) {
        try {
            Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/art_gal_db",
                "root",
                "minh152005minh"
            );
            System.out.println("✅ Kết nối thành công!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
