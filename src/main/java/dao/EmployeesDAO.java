package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import dto.EmployeeDTO;

public class EmployeesDAO {

	private static final String URL = "jdbc:sqlserver://localhost\\SQLEXPRESS;database=example";
	private static final String USERNAME = "sa";
	private static final String PASSWORD = "shiroishi";

	public List<EmployeeDTO> findAll() {
		
		// 戻り値格納用のリスト
		List<EmployeeDTO> empList = new ArrayList<>();

		// JDBCドライバを読み込む
		try {
			Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
		} catch (ClassNotFoundException e) {
			throw new IllegalStateException("JDBCドライバを読み込めませんでした");
		}
		// データベースに接続
		try (Connection conn = DriverManager.getConnection(URL, USERNAME, PASSWORD)) {

			// SELECT文を準備
			String sql = "SELECT ID,NAME,AGE FROM EMPLOYEES";
			PreparedStatement pStmt = conn.prepareStatement(sql);

			// SELECTを実行し、結果表（ResultSet）を取得
			ResultSet rs = pStmt.executeQuery();

			// 結果表に格納されたレコードの内容を表示
			while (rs.next()) {
				String id = rs.getString("ID");
				String name = rs.getString("NAME");
				int age = rs.getInt("AGE");
				
				EmployeeDTO employee = new EmployeeDTO(id, name, age);
				empList.add(employee);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return empList;

	}
}
